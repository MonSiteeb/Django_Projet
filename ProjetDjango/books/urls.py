
from books.views import index, subscribe, inscription, document, logout,login
from books.views import index, subscribe, inscription, liste_docs
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    # path('', views.index, name='index'),
    path("",index,name="index"),
    # liste des documents
    path("documents",liste_docs,name="documents"),

    path('inscription',inscription,name='inscription'),
    
    path('contact',subscribe,name='contact'),
    # ajout de document
    path('document',document,name='document'),

    path('logout',logout,name='logout'),
    path('login',login,name='login'),

]

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
