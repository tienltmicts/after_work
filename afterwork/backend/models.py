import datetime
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from afterwork.settings import *
# Create your models here.

class Subscribers(models.Model):
    class Meta:
        db_table = "subscribers"
        verbose_name = 'Subscribers'
        verbose_name_plural = 'Subscribers'
    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=255)
    current_address = models.TextField()
    position = models.CharField(max_length=255)
    status = models.BooleanField("Active?", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    class Meta:
        db_table = "room"
        verbose_name = 'Room'
        verbose_name_plural = 'Room'
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return str(self.name) + "-" + str(self.address)

class TimeSubjects(models.Model):
    class Meta:
        db_table = "time_and_subjects"
        verbose_name = 'TimeSubjects'
        verbose_name_plural = 'TimeSubjects'
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
    time = models.CharField(
        max_length=255,
        choices=TIME_CHOICE,
        default='1'
    )
    DAY_CHOICE= (
        ('Thứ 2', 'Thứ 2'),
        ('Thứ 3', 'Thứ 3'),
        ('Thứ 4', 'Thứ 4'),
        ('Thứ 5', 'Thứ 5'),
        ('Thứ 6', 'Thứ 6'),
        ('Thứ 7', 'Thứ 7'),
        ('Chủ nhật', 'Chủ nhật'),
    )
    day_of_week = models.CharField(
        max_length=255,
        choices=DAY_CHOICE,
        default='1'
    )
    teacher = models.ManyToManyField(Subscribers, related_name="list_subscribers", blank=True)
    room = models.ManyToManyField(Room, related_name="list_room", blank=True)
    start_date = models.DateField('Ngay bat dau',null=True, blank=True)
    end_date = models.DateField('Ngay ket thuc',null=True, blank=True)

class Subjects(models.Model):
    class Meta:
        db_table = "subjects"
        verbose_name = 'Subjects'
        verbose_name_plural = 'Subjects'
    name = models.CharField(max_length=255)
    LEVEL_CHOICE= (
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
    )
    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICE,
        default='14'
    )
    time = models.ManyToManyField(TimeSubjects, related_name="list_timesubject", blank=True)
    


# class ScheduleTeach(models.Model):
#     class Meta:
#         db_table = "schedule_teach"
#         verbose_name = 'ScheduleTeach'
#         verbose_name_plural = 'ScheduleTeach'
#     schedule = models.OneToOneField( TimeSubjects, on_delete=models.CASCADE)
#     teacher = models.OneToOneField(Subscribers, on_delete=models.CASCADE)

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
    LEVEL_CHOICE= (
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
    created_at = models.DateTimeField()
    start_date = models.DateField('Ngay bat dau',null=True, blank=True)
    end_date = models.DateField('Ngay ket thuc',null=True, blank=True)
    
class ScheduleLearn(models.Model):
    class Meta:
        db_table = "schedule_learn"
        verbose_name = 'ScheduleLearn'
        verbose_name_plural = 'ScheduleLearn'
    subject = models.OneToOneField(
        Subjects,
        on_delete=models.CASCADE
    )
    time = models.OneToOneField(TimeSubjects, on_delete=models.CASCADE)
    student = models.ForeignKey("backend.Subscribers", null=True, blank=True, related_name='student', on_delete=models.CASCADE)

class Comments(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'

    sender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True, blank=True)