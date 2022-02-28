from books.views import index, subscribe, inscription, document, logout
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    # path('', views.index, name='index'),
    path("",index,name="index"),
    path('inscription',inscription,name='inscription'),
    path('contact',subscribe,
         name='contact'),

    path('document',document,name='document'),

    path('logout',logout,name='logout'),



]

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
