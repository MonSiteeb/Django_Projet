from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def inscription(request):
    return render(request,'inscription.html') 

def ajoutEpreuve(request):
    return render(request,'ajout_epreuve.html') 