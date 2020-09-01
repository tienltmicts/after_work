from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import datetime
# Create your models here.

class Subscribers(models.Model):
    class Meta:
        db_table = "subscribers"
        verbose_name = 'Subscribers'
        verbose_name_plural = 'Subscribers'

    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    # shareholder = models.OneToOneField('ShareHolder', on_delete=models.CASCADE)
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

class Time_of_day(models.Model):
    class Meta:
        db_table = "time_of_day"
        verbose_name = 'Time_of_day'
        verbose_name_plural = 'Time_of_day'
    TIME_CHOICE = (
        ('7h','7h'),
        ('8h', '8h'),
        ('9h','9h'),
        ('10h', '10h'),
        ('11h','11h'),
        ('14h','14h'),
        ('15h', '15h'),
        ('16h','16h'),
        ('17h', '17h'),
        ('18h', '18h'),
        ('19h', '19h'),
        ('20h','20h')
    )
    start_time = models.CharField(
        max_length=255,
        choices=TIME_CHOICE,
        default='7h'
    )
    end_time = models.CharField(
        max_length=255,
        choices=TIME_CHOICE,
        default='9h'
    )
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

class Room(models.Model):
    class Meta:
        db_table = "room"
        verbose_name = 'Room'
        verbose_name_plural = 'Room'
    name = models.CharField(max_length=255)
    address = models.TextField()

class TimeSubjects(models.Model):
    class Meta:
        db_table = "time_and_subjects"
        verbose_name = 'TimeSubjects'
        verbose_name_plural = 'TimeSubjects'

    time = models.OneToOneField(Time_of_day, on_delete=models.CASCADE)
    subjects = models.OneToOneField(Subjects, on_delete=models.CASCADE)
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
    room = models.OneToOneField(Room, on_delete=models.CASCADE)

class ScheduleTeach(models.Model):
    class Meta:
        db_table = "schedule_teach"
        verbose_name = 'ScheduleTeach'
        verbose_name_plural = 'ScheduleTeach'
    schedule = models.OneToOneField( TimeSubjects, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Subscribers, on_delete=models.CASCADE)

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
    schedule = models.ManyToManyField(
        ScheduleTeach,
        blank=True
    )
    student = models.OneToOneField(Subscribers, on_delete=models.CASCADE)
