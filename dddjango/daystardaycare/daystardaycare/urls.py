"""
URL configuration for daystardaycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from firstlanding.views import firstlanding
from secondlanding.views import secondlanding
from adminsignin.views import adminsignin
from cashiersignin.views import cashiersignin
from adminsecsignin.views import adminsecsignin
from usercreation.views import usercreation
from babyregistration.views import babyregistration


urlpatterns = [
    path("", firstlanding, name="home"),
    path("secondlanding/", secondlanding, name="general page"),
    path("adminsignin/", adminsignin, name="adminsignin"),
    path("cashiersignin/", cashiersignin, name="cashiersignin"),
    path("adminsecsignin/", adminsecsignin, name="adminsecsignin"),
    path("usercreation/", usercreation, name="usercreation"),
    path("babyregistration/", babyregistration, name="babyregistration"),
]
