from django import forms
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from ProjetDjango.settings import LOGIN_REDIRECT_URL
from books.forms import UserForm
from django.contrib.auth import login
from django.contrib.auth import logout

from ProjetDjango.settings import EMAIL_HOST_USER
from books.forms import DocumentForm,Subscribe
from books.models import Document, User
from django.contrib import auth




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
                request, 'afterlogin.html',
                # template_name=template_name,
            {'form':form})
            

# def document(request): 
#     # ajout document
#     #now it is empty book form for sending to html
#     form=DocumentForm()
#     if request.method=='POST':
#         #now this form have data from html
#         form=DocumentForm(request.POST , request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request,'docajouter.html',{'form':form})
#     return render(request,'document.html',{'form':form})


def document(request, *args, **kwargs):
    template_name = 'document.html'
    
    obj = Document()

    if request.method == 'GET':
        form = DocumentForm()
        context = {
            'form': form
        }

        return render(
            request=request,
            template_name=template_name,
            context=context
        )

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.matiere = form.cleaned_data.get('matiere')
            obj.classe = form.cleaned_data.get('classe')
            obj.professeur = form.cleaned_data.get('professeur')
            obj.categorie = form.cleaned_data.get('type')
            obj.fichier = form.cleaned_data.get('fichier')
            obj.save()
            redirect('index')
        return render(
    
        request=request,
            template_name=template_name,
            context=context
        )



def afterlogin(request):
        return render(request,'afterlogin.html')

def liste_docs(request,*args, **kwargs):
    docs = Document.objects.all()
    context = {
        'docs' : docs,
               }
    return render(request, 'liste_documents.html', context=context)


# def logout(request):
#     return render(request,'index.html')
