from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Register your models here.
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'email', 'current_address', 'position', 'status', 'created_at','updated_at')
    search_field = ('name')

admin.site.register(Subscribers, SubscribersAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

admin.site.register(Subjects, SubjectsAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Room, RoomAdmin)

class TimeSubjectsAdmin(admin.ModelAdmin):
    list_display = ( 'time',  'day_of_week','get_room', 'get_teacher')

    def get_room(self, obj):
        return mark_safe("<br/>".join([str(m.name) + "-" + str(m.address) for m in obj.room.all()]))
    get_room.short_description = 'Room'

    def get_teacher(self, obj):
        return mark_safe("<br/>".join([m.name for m in obj.teacher.all()]))
    get_teacher.short_description = 'Teacher'

admin.site.register(TimeSubjects, TimeSubjectsAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'level', 'created_at', 'start_date', 'end_date')
    search_field = ('')
    def get_user(self, obj):
        return obj.user.name
    get_user.short_description = 'Teacher'

admin.site.register(Teacher, TeacherAdmin)

class ScheduleLearnAdmin(admin.ModelAdmin):
    list_display = ('get_subject','get_time', 'get_student')
    def get_subject(self, obj):
        return str(obj.subject.name)
    get_subject.short_description = 'Subject'
    def get_time(self, obj):
        return mark_safe("".join(str(obj.time.day_of_week) + ' Kip ' + str(obj.time.time)))
    get_time.short_description = 'Lich hoc'

    def get_student(self, obj):
        return str(obj.student.name)
    get_student.short_description = 'Student'

admin.site.register(ScheduleLearn, ScheduleLearnAdmin)