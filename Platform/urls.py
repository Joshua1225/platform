"""Platform URL Configuration

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
from backends import views, Search_views
from backends.forms import MySearchForm

from django.urls import path,include
from backends import views,keywordview,paperview,messageview,user,expertview

urlpatterns = [

    path('', views.test ),
    path('upload_paper',paperview.upload_paper),
    path('download_paper',paperview.download_paper),

    path('appeal',messageview.appeal),

    path('editacademia',expertview.editacademia),
    path('follow', user.follow),
    path('collect', user.collect),
    path('userinfo', user.userinfo),
    path('login',user.login),
    path('logout',user.logout),
    path('register',user.register),
    path('change_info',user.change_info),
    path('check_login',user.check_login),
    path('data', views.data),
    path('getkeyword', keywordview.getkeyword),
    path('search/', Search_views.MySearchView(form_class=MySearchForm),
         name='haystack_search')

]
