from django.urls import path

from . import user

app_name = 'backends'
urlpatterns = [
    path('login/', user.login),
    path('logout/', user.logout),
    path('register/', user.register)
]