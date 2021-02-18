#this file is not given to us,we have to create it everytime we create django app
from django.urls import path

from . import views# . means current directory

urlpatterns=[
    path("",views.index,name="index")
    
]
