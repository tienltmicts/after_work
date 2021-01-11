from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user-login/$',views.user_login,name='user_login'),
    path('comment/', views.comment, name='comment'),
    path('update-profile/', views.update_profile, name='update_profile'),
    #student
    path('register-subjects/', views.register_subjects, name='register_subjects'),
    path('register-subjects-detail/<int:id>/', views.register_subjects_detail, name='register_subjects_detail'),
    path('create-time-table/<int:id>/', views.create_time_table, name='create_time_table'),
    path('exit-time-table/<int:id>/', views.exit_time_table, name='exit_time_table'),
    path('view-time-table/', views.view_time_table, name='view_time_table'),
    path('search-subjects/', views.search_subject, name='search_subject'),
    path('view-tkb/', views.view_tkb, name='view_tkb'),
    path('view-tkb-list-subjects/', views.tkb_list_subjects, name='tkb_list_subjects'),
    path('view-student-list/<int:id>/', views.view_students_list, name='view_students_list'),
    path('download-student-list/<int:id>/', views.download_students_list, name='download_students_list'),
    #teacher
    path('create-subject/', views.register_subjects_teach, name='register_subjects_teach'),
    path('create-schedule/', views.create_time_subject, name='create_time_subject')
]