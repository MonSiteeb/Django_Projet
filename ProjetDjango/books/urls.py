from books.views import index, subscribe
from django.urls import path

urlpatterns = [
    path("",index,name="home"),
    path('contact',subscribe,
         name='contact')
]
