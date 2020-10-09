from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    phone = models.CharField(max_length=255)
    current_address = models.TextField()
    POSITION_CHOICE= (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    position = models.CharField(
        max_length=255,
        choices=POSITION_CHOICE,
        default='student'
    )
    status = models.BooleanField("Active?", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username