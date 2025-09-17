from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('base/', views.base, name='base'),
    path('todo/', views.todo, name='todo'),
]

