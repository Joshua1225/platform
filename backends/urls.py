from django.urls import path

from . import user, views

app_name = 'backends'
urlpatterns = [
    path('test', views.test),
    path('changeinfo', user.change_info),
    path('login', user.login),
    path('logout', user.logout),
    path('register', user.register),
    path('follow', user.follow),
    path('collect', user.collect),
    path('userinfo', user.userinfo)
]