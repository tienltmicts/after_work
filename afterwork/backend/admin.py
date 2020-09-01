from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Register your models here.
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'email', 'current_address', 'position', 'status', 'created_at','deleted_at')
    search_field = ('name')

admin.site.register(Subscribers, SubscribersAdmin)

class TimeOfDayAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')

admin.site.register(Time_of_day,TimeOfDayAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

admin.site.register(Subjects, SubjectsAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Room, RoomAdmin)

class TimeSubjectsAdmin(admin.ModelAdmin):
    list_display = ('get_time', 'get_subject', 'day_of_week','get_room')
    def get_time(self, obj):
            return str(obj.time.start_time)+'-'+ str(obj.time.end_time)
    get_time.short_description = 'Kíp'

    def get_subject(self, obj):
        return str(obj.subjects.name)
    get_subject.short_description = 'Subjects'
    def get_room(self, obj):
        return str(obj.room.name)
    get_room.short_description = 'Room'

admin.site.register(TimeSubjects, TimeSubjectsAdmin)

class ScheduleTeachAdmin(admin.ModelAdmin):
    list_display = ('get_schedule', 'get_teacher', 'get_room')

    def get_schedule(self, obj):
        return str(obj.schedule.day_of_week) + ' Kip ' + str(obj.schedule.time.start_time)+'-'+ str(obj.schedule.time.end_time)
    get_schedule.short_description = 'Schedule'
    def get_teacher(self, obj):
        return str(obj.teacher.name)
    get_teacher.short_description = 'Teacher'

    def get_room(self, obj):
        return str(obj.schedule.room.name)
    get_room.short_description = 'Room'

admin.site.register(ScheduleTeach, ScheduleTeachAdmin)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'level', 'created_at', 'start_date', 'end_date')
    search_field = ('')
    def get_user(self, obj):
        return obj.user.name
    get_user.short_description = 'Teacher'

admin.site.register(Teacher, TeacherAdmin)

class ScheduleLearnAdmin(admin.ModelAdmin):
    list_display = ('get_schedule', 'get_student')
    def get_schedule(self, obj):
        return mark_safe("<br/>".join([str(m.schedule.day_of_week) + ' Kip ' + str(m.schedule.time.start_time)
            +'-'+ str(m.schedule.time.end_time) + "- Nguoi day: "+ str(m.teacher.name)  
            + '- Phong: ' + str(m.schedule.room.name) for m in obj.schedule.all()]))
    get_schedule.short_description = 'Lich hoc'

    def get_student(self, obj):
        return str(obj.student.name)
    get_student.short_description = 'Student'

admin.site.register(ScheduleLearn, ScheduleLearnAdmin)