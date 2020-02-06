"""myproject URL Configuration

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
from django.conf.urls import url
from armyapp.views import *



urlpatterns = [
    url(r'^$', homepage),
    url(r'^addnew$', addnew),
    url(r'^addstock$', addstock),
    url(r'^stocktable$', stocktable),
    url(r'^issueregister$', issueregistershow),
    url(r'^loadchart$', loadchartshow),
    url(r'^issueaction/(?P<userid>[\w-]+)/$', issueaction),
    url(r'^submitissue$', submitissue),
    url(r'^test$', test),
    url(r'^sd/(?P<depoid>[\w-]+)/$', deposhow),
    url(r'^login$', login),
    url(r'^loginaction$', loginaction),
    url(r'^logout$', logout),

]
