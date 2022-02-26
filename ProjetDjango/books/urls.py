from books.views import index, subscribe
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path("",index,name="index"),
    path('contact',subscribe,
         name='contact')
]
