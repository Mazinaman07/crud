from django.urls import path

from . views import *




urlpatterns = [
    
    path('',index),
    
    path('loaditem/',loaditem),
    path('additem/',additem),
    path('showitem/',showitem),

    path('edititem/<int:id>',edititem),
    path('updateitem/<int:id>',updateitem),
    path('deleteitem/<int:id>',deleteitem),

    path('edituser/<int:id>',edituser),
    path('deleteuser/<int:id>',deleteuser),
    path('updateuser/<int:id>',updateuser),

    path('adduser/',adduser),
    path('adduserform/',adduserform),
    path('loaduser/',loaduser),
    
]