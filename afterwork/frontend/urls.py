from django.urls import path
from django.conf.urls import url

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('signup/', views.signup, name='signup'),
#     url(r'^login', views.view_login, name='login'),
#     url(r'^logout', views.view_logout, name='logout'),
# ]
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]