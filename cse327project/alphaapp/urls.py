
from django.urls import path
from . import views
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('main/', views.main, name="main"),
    path('faq/', views.faq, name="faq"),
]


