from django import forms
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from ProjetDjango.settings import EMAIL_HOST_USER
from books.forms import DocumentForm,Subscribe
from books.models import Document, User

# Create your views here.
def index(request,*args, **kwargs):
    template_name = "index.html"
    users = User.objects.all()
    docs = Document.objects.all()
    context = {
        'docs' : docs,
        'users' : users,
               }
    return render(request=request, template_name=template_name, context=context)

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Bienvenue cher abonné'
        message = 'Ce mail a été envoyé automatiquement'
        recepient = str(sub['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return render(request, 'contact.html', {'form':sub})