"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render

def func(request):
    return render(request,'index.html')
def func1(request):
    return render(request, 'pyt.html')
def step(request, d,c):
    return HttpResponse(int(d)**(int(c)))
def inside(request , r ,t):
    return HttpResponse(int(r)//int(t))

urlpatterns= [
    url(r'^admin/', admin.site.urls),
    url(r'^$', func),
    url(r'^step/(?P<d>\w+)/(?P<c>\w+)$', step),
    url(r'^inside/(?P<r>\w+)/(?P<t>\w+)$', inside),
    url(r'^main/$' , func1)
]
