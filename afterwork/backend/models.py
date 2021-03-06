import datetime
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from afterwork.settings import *
# Create your models here.

USER_PROFILE_GENDER_CHOICES = [
        (0, 'Khác'),
        (1, 'Nam'),
        (2, 'Nữ'),
    ]
LEVEL_CHOICE= [
        ('1', 'Lớp 1'),
        ('2', 'Lớp 2'),
        ('3', 'Lớp 3'),
        ('4', 'Lớp 4'),
        ('5', 'Lớp 5'),
        ('6', 'Lớp 6'),
        ('7', 'Lớp 7'),
        ('8', 'Lớp 8'),
        ('9', 'Lớp 9'),
        ('10', 'Lớp 10'),
        ('11', 'Lớp 11'),
        ('12', 'Lớp 12'),
        ('13', 'Sinh viên'),
        ('14', 'Đang đi làm'),
]
POSITION = [
    ('0', 'Student'),
    ('1', 'Teacher')
]
DAY_CHOICE= (
        ('Thứ 2', 'Thứ 2'),
        ('Thứ 3', 'Thứ 3'),
        ('Thứ 4', 'Thứ 4'),
        ('Thứ 5', 'Thứ 5'),
        ('Thứ 6', 'Thứ 6'),
        ('Thứ 7', 'Thứ 7'),
        ('Chủ nhật', 'Chủ nhật'),
    )
TIME_CHOICE = (
        ('1','7h - 9h'),
        ('2', '9h - 11h'),
        ('3','14h - 16h'),
        ('4', '16h - 18h'),
        ('5','18h - 20h'),
        ('6','17h - 19h'),
        ('7', '19h - 21h'),
        ('8','18h - 19h'),
    )
class Subscribers(models.Model):
    class Meta:
        db_table = "subscribers"
        verbose_name = 'Subscribers'
        verbose_name_plural = 'Subscribers'
    uid = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    gender = models.PositiveSmallIntegerField(_('Gender'), choices=USER_PROFILE_GENDER_CHOICES, default=0)
    id_selfie = models.ImageField(_('Selfie'),upload_to="media/profile",default = 'media/profile/None/no-img.jpg')
    current_address = models.TextField()
    position = models.CharField(
        max_length=255,
        choices=POSITION,
        default='1'
    )
    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICE,
        default='14'
    )
    status = models.BooleanField("Active?", default=True)
    created_at = models.DateTimeField(_('Created'),auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(_('Updated'),auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.name) 

class Room(models.Model):
    class Meta:
        db_table = "room"
        verbose_name = 'Room'
        verbose_name_plural = 'Room'
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return str(self.name)

class TimeSubjects(models.Model):
    class Meta:
        db_table = "time_and_subjects"
        verbose_name = 'TimeSubjects'
        verbose_name_plural = 'TimeSubjects'
    
    time = models.CharField(
        max_length=255,
        choices=TIME_CHOICE,
        default='1'
    )
    
    day_of_week = models.CharField(
        max_length=255,
        choices=DAY_CHOICE,
        default='1'
    )
    start_date = models.DateField('Ngay bat dau',null=True, blank=True)
    end_date = models.DateField('Ngay ket thuc',null=True, blank=True)

    def __str__(self):
        return "Kíp: " + str(self.time) +"-" + str(self.day_of_week)

class Subjects(models.Model):
    class Meta:
        db_table = "subjects"
        verbose_name = 'Subjects'
        verbose_name_plural = 'Subjects'
    name = models.CharField(max_length=255)
    
    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICE,
        default='14'
    )
    def __str__(self):
        return str(self.name)+'-'+ str(self.level) 

class Teacher(models.Model):
    class Meta:
        db_table = "teacher"
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teacher'
    user = models.OneToOneField(
        Subscribers,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICE,
        default='14'
    )
    subjects_teach = models.ManyToManyField(
        Subjects,
        related_name="list_subjects",
        blank=True
    )
    schedule_registere = models.ManyToManyField(
        TimeSubjects,
        related_name="list_timeSubjects",
        blank=True
    )
    start_date = models.DateField('Ngay bat dau',null=True, blank=True)
    note = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return str(self.user)
    
class ScheduleTeach(models.Model):
    class Meta:
        db_table = "schedule_teach"
        verbose_name = 'ScheduleTeach'
        verbose_name_plural = 'ScheduleTeach'
    groubId = models.CharField(max_length=255)
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, blank=True)
    time = models.ForeignKey(
        TimeSubjects, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return str(self.groubId)

class ScheduleLearn(models.Model):
    class Meta:
        db_table = "schedule_learn"
        verbose_name = 'ScheduleLearn'
        verbose_name_plural = 'ScheduleLearn'
    schedule = models.OneToOneField(
        ScheduleTeach,
        on_delete=models.CASCADE,
        null=True
    )
    student = models.ManyToManyField(Subscribers, related_name="learn_students", blank=True)

    def __str__(self):
        return str(self.schedule)

class Comments(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'

    sender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True, blank=True)

class TKB(models.Model):
    class Meta:
        db_table ="TKB"
        verbose_name = "TKB"
        verbose_name_plural = "TKB"
    
    schedule_learn = models.ManyToManyField(ScheduleLearn, related_name="tkb_schedule", blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )