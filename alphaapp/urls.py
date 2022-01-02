from django.contrib.messages.api import success
from django.urls import path
from . import views
from .views import Signup, SellerSignupVIew, CustomerSignUpView

urlpatterns = [
    path('main/', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('log/', views.log, name="log"),
    path('success/', views.welcome, name='success'),
    path('log2/', views.log2, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.Signup, name='signup'),
    path('faq/', views.FAQ, name='faq'),
    path('userprofile/', views.UserProfile, name='user-profile'),
    path('contact/', views.Contact, name='contact'),
    path('alphaapp/signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('alphaapp/signup/seller/',   SellerSignupVIew.as_view(),  name='seller_signup'),
]