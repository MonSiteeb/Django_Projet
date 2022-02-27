from books.views import index, subscribe, inscription
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    # path('', views.index, name='index'),
    path("",index,name="index"),
    path('inscription',inscription,name='inscription'),
    path('contact',subscribe,
         name='contact'),
]

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
