from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user-login/$',views.user_login,name='user_login'),
]