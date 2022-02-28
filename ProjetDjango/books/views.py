from django import forms
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from ProjetDjango.settings import LOGIN_REDIRECT_URL
from books.forms import UserForm
from django.contrib.auth import login
from ProjetDjango.settings import EMAIL_HOST_USER
from books.forms import DocumentForm,Subscribe
from books.models import Document, User

# Create your views here.
def index(request,*args, **kwargs):
    users = User.objects.all()
    docs = Document.objects.all()
    context = {
        'docs' : docs,
        'users' : users,
               }
    return render(request, 'index.html', context=context)

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Bienvenue cher abonné'
        message = 'Ce mail a été envoyé automatiquement'
        recepient = str(sub['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'contact.html', {'form':sub})

def inscription(request,*args, **kwargs):
    template_name = 'inscription.html'
    obj = User()
    if request.method == 'GET':
        form = UserForm()
        context = {'form':form}
    
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = UserForm(
            request.POST,
            request.FILES
            ) 
        context = {'form':form}
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request,user)
            redirect(LOGIN_REDIRECT_URL)
        return render(
                request=request,
                template_name=template_name,
                context=context
            )
def liste_docs(request,*args, **kwargs):
    docs = Document.objects.all()
    context = {
        'docs' : docs,
               }
    return render(request, 'liste_documents.html', context=context)
