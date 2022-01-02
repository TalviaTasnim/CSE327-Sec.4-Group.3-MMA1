from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from .models import *

# Create your views here.


def main(request):
    return render (request, 'main.html')

def contact(request):
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
    already_answers=Question.objects.filter(answered=True)
    without_answers=Question.objects.filter(answered=False)
    answer_contents=Answer.objects.all()
    context={
        'already_answers':already_answers,
        'without_answers':without_answers,
        'answer_contents':answer_contents
    }
    return render(request, 'faq.html', context)