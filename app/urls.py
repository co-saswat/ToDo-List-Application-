"""sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("index",views.index, name="home"),
    path("delete/<list_id>/", views.delete , name="delete"),
    path("cross_off/<list_id>/", views.cross_off , name="cross_off"),
    path("uncross/<list_id>/", views.uncross , name="uncross"),
    path("edit/<list_id>/",views.edit, name="edit"),
]
