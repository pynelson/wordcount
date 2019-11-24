from .import views
from django.urls import path

urlpatterns = [

    path('', views.Indexpage, name='index'),
    path('count/', views.countpage, name='count'),
    path('again/', views.startagain, name = 'index'),
    path('about/', views.aboutpage, name ='about'),
    path("contact/", views.contactpage, name="contact")

]
