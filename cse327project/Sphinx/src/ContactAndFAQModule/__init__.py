""""


"""



def main(request):
    
    
    return render (request, 'main.html')

def contact(request):
    
    """
    this is a contact page which has a contact page 
    :param request: httpresponse  from users
    :return type: returns a contact page for view
    :type request: httpResponse
    
    
    """
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()


        send_mail(
             'message from' + name,
             subject,
             email,
             ['anjoomopshora@gmail.com'],

        )
        return render(request, 'contact.html', {'name' : name})
    else:
        return render(request, 'contact.html',{})


def faq(request):
    
    """
    this is a a FAQ page which has a questions and answer page 
    :param request: httpresponse  from users
    :return type: returns a FAQ page for view
    :type request: httpResponse
    
    
    """
    already_answers=Question.objects.filter(answered=True)
    without_answers=Question.objects.filter(answered=False)
    answer_contents=Answer.objects.all()
    context={
        'already_answers':already_answers,
        'without_answers':without_answers,
        'answer_contents':answer_contents
    }
    return render(request, 'faq.html', context)

