"""
  
LoginRegisterModule
-----------------------------

This is a module whcih has a function
for customer and seller logn and registartion and viweing Details


"""



# Create your views here.


def cutomer_log(request):

    """
    This method is used to view the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username =request.POST.get('customer_name')
            password =request.POST.get('customer_password')
            
            user= authenticate(request, username=username, password=password)

            if user is not None and user.is_customer:
                login(request, user)
                return redirect('profile')
            elif user is not None and user.is_seller:
                messages.info(request, 'This  is for customers only, You are a Seller')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
    context= {}
    return render(request, 'login.html', context)


def seller_log2(request):
    """
    This method is used to view the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    
    if request.user.is_authenticated:
        return redirect('success')
    else:
        if request.method == 'POST':
            username =request.POST.get('seller_name')
            password =request.POST.get('seller_password')
            user= authenticate(request, username=username, password=password)

            if user is not None and user.is_seller:
                login(request, user)
                return redirect('main')
            elif user is not None and user.is_customer:
                messages.info(request, 'This  is for Sellers only, You are a Customer')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
    context= {}
    return render(request, 'login.html', context)

def UserProfile(request): 
    """
    This method is used to view the user prfile login.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    username_c=request.user.username
    user_c=request.user
    ccuser=Customer.objects.all()
    context={'ccuser':ccuser}
    return render (request, 'userprofile.html', context)


def log_out(request):
    """
    This method is used to logout page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns the user in home  page which is a HTML page.
    :rtype: HttpResponse.
    """
    logout(request)
    return redirect('log')



def main(request):

    """
    This method is used to view the main page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns the main page which is a HTML page.
    :rtype: HttpResponse.
    """
    return render(request, 'main.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    """
    This method is used to view the login page as a seller or customer .
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a login page which is a HTML page.
    :rtype: HttpResponse.
    """
    return render(request, 'login.html')

def Signup(request):
    """
    This method is used to view the registtartion page as a seller or customer .
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a signup page which is a HTML page.
    :rtype: HttpResponse.
    """
    return render(request, 'register.html')
def welcome(request):
    """
    This method is used to view succesfull login and registartion .
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a welcome page which is a HTML page.
    :rtype: HttpResponse.
    """
    return render(request, 'success.html')








