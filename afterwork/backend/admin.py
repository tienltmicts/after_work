from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Register your models here.
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'email','birthday','gender', 'current_address', 'position', 'status', 'created_at','updated_at')
    search_field = ('name')

admin.site.register(Subscribers, SubscribersAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

admin.site.register(Subjects, SubjectsAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Room, RoomAdmin)

class TimeSubjectsAdmin(admin.ModelAdmin):
    list_display = ( 'time',  'day_of_week')

admin.site.register(TimeSubjects, TimeSubjectsAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_teacher', 'level','get_subject_teach','get_schedudle', 'start_date', 'note')
    # search_field = ('')
    def get_teacher(self, obj):
        return obj.user.name
    get_teacher.short_description = 'Teacher'

    def get_subject_teach(self,obj):
        return mark_safe("<br/>".join([m for m in obj.subjects_teach.all()]))
    get_subject_teach.short_description = 'Subjects Registed To Teach'

    def get_schedudle(self,obj):
        return mark_safe("<br/>".join([m for m in obj.schedule_registere.all()]))
    get_schedudle.short_description = 'Schedule Registed To Teach'

admin.site.register(Teacher, TeacherAdmin)

class ScheduleTeachAdmin(admin.ModelAdmin):
    list_display =('groubId', 'subject','room','teacher')

admin.site.register(ScheduleTeach, ScheduleTeachAdmin)

class ScheduleLearnAdmin(admin.ModelAdmin):
    list_display = ('get_schedudle',)
    def get_schedudle(self, obj):
        return  obj.schedule
    get_schedudle.short_description = 'Group Schedule'
    

admin.site.register(ScheduleLearn, ScheduleLearnAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('sender','email', 'comment', 'sent_date')

admin.site.register(Comments, CommentsAdmin)

class TKBAdmin(admin.ModelAdmin):
    list_display = ('get_schedule_learn', 'user')
    def get_schedule_learn(self, obj):
        return mark_safe("<br/>".join([str(m.schedule.subject) for m in obj.schedule_learn.all()]))
    get_schedule_learn.short_description = 'Schedule Learn'

admin.site.register(TKB, TKBAdmin)