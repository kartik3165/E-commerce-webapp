from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('about', views.about , name = "about"),
    path('shop', views.shop , name = "shop"),
    path('furniture', views.furniture , name = "furniture"),
    path('contact', views.contact , name = "contact"),
    path('allproduct', views.allproduct , name = "allproduct"),
    path('auth', views.auth , name = "auth"),
    path('login', views.signin , name = "login"),
    path('signup', views.signup , name = "signup"),
    path('logout', views.log , name = "logout")
]