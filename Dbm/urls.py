"""Dbm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from god import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view()),
    url(r'^dbbackup/', include('god.urls', namespace='god')),

    url(r'^api/saveDB/', views.saveDB, name='saveDB'),
    url(r'^api/addTestIp/', views.addTestIp, name="addtestip"),
    url(r'^api/online/', views.online, name='online'),
    url(r'^api/offline/(?P<game>\w+)/', views.offline, name='offline'),
    url(r'^api/checkBackupStatus/', views.checkBackupStatus, name='checkBackupStatus'),
]
