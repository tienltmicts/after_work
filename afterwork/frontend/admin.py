from django.contrib import admin

# Register your models here.
from .models import UserProfileInfo, User

admin.site.register(UserProfileInfo)