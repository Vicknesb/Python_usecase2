from django.urls import path
from . import views

urlpatterns =[
    path("login/", views.login),
    path("register", views.signup),
    path("logout/", views.logout, name='logout'),
]
