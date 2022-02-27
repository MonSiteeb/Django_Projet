from books.views import index, subscribe, inscription
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path("",index,name="index"),
    path('inscription',inscription,name='inscription'),
    path('contact',subscribe,
         name='contact'),
]
