from django.urls import path
from . import views

urlpatterns=[
    path('',views.gallary,name='gallary'),
    path('photo/<str:pk>/',views.viewPhoto,name='photo'), #we want to add photos by id so we add primary key as string pk
    path('add/',views.addPhoto,name='add'),
]