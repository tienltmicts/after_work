from .forms import (
    LoginForm,
    RegisterForm,
    CommentForm,
    UpdateProfileForm,
    RegisterSubjectsForm,
    FilterTKBForm
)
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from backend.models import *
import datetime
from django.db.models import Q
from django.utils.timezone import utc
import csv
import time

def index(request):
    sub = get_object_or_404(Subscribers, uid=request.user)
    return render(request,'index.html', {'sub': sub})
def home(request):
    return render(request,'base.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")

def register(request):
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                
                sub = Subscribers.objects.create(
                    uid=user,
                    name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    birthday= datetime.datetime.now(),
                    phone=form.cleaned_data['phone_number'],
                    position=form.cleaned_data['position'],
                    current_address='',
                    level = request.POST.get('level'),
                    status=True,
                )
                sub.save()
                tkb = TKB.objects.create(user=user)
                tkb.save()
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/home')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form, 'position': POSITION, 'level':LEVEL_CHOICE})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session.set_expiry(0)
                login(request, user)
                return HttpResponseRedirect('/home')
            if request.POST['remember_me']:
                request.session.set_expiry(30)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def password_change(request):
    sub = get_object_or_404(Subscribers, uid=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form,
        'sub': sub
    })

def comment(request):
    template = 'comments.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # Create the comment:
            comment = Comments.objects.create(
                sender=request.POST.get('sender'),
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment'],
                sent_date = datetime.datetime.now()
            )
            comment.save()
            update_session_auth_hash(request, comment)  # Important!
            messages.success(request, 'Your comment was successfully sent!')
            return redirect('/home')
        else: messages.error(request, 'Please correct the error below.')
   # No post data availabe, let's just show the page.
    else:
        form = CommentForm()

    return render(request, template, {'form': form})

@login_required
def update_profile(request):
    template = 'update_profile.html'

    sub = get_object_or_404(Subscribers,uid=request.user)
    if request.method == 'POST' :
        form = UpdateProfileForm( request.POST) 
        if form.is_valid():
            print(request.FILES.get('id_selfie'))
            Subscribers.objects.filter(uid=request.user).update(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                birthday=request.POST.get('birthday'),
                phone = request.POST.get('phone'),
                gender = request.POST.get('gender'),
                current_address= request.POST.get('current_address'),
                position= request.POST.get('position'),
                level = request.POST.get('level'),
                updated_at= datetime.datetime.now().replace(tzinfo=utc)
            )
            if  'id_selfie' in request.FILES or request.POST.get('id_selfie-clear'):
                user = Subscribers.objects.get(uid= request.user)
                user.id_selfie = request.FILES.get('id_selfie')
                user.save()
            messages.success(request, 'Your profile was successfully update!')
            return redirect('/home')
        else: messages.error(request, 'Please correct the error below.')
   # No post data availabe, let's just show the page.
    else:
        form = UpdateProfileForm(
            initial={
                    'name' : sub.name,
                    'email' : sub.email,
                    'birthday' : sub.birthday,
                    'phone': sub.phone,
                    'gender' : sub.gender,
                    'id_selfie' : sub.id_selfie,
                    'current_address' : sub.current_address,
                    'position' : sub.position,
                    'level': sub.level
                }
        )
    return render(request, template, {
        'form': form,
        'sub': sub,
        "genders": USER_PROFILE_GENDER_CHOICES,
        'position': POSITION,
        'level': LEVEL_CHOICE
        })

@login_required
def register_subjects(request):
    sub = get_object_or_404(Subscribers, uid=request.user)
    if request.method == 'GET':
        subj = Subjects.objects.filter(level=sub.level)
        return render(request,'register_subjects/register_subjects.html',{
            'subj': subj,
            'sub': sub
        })

@login_required
def search_subject(request):
    sub = get_object_or_404(Subscribers, uid=request.user)
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string=request.GET.get('q')
        seens=Subjects.objects.filter(
            Q(name__icontains=query_string) | 
            Q(id__icontains=query_string)   
        )
    else:
        seens=None
    return render(request, 'register_subjects/search_subject.html', {
            "subjects": seens,
            "query_string": query_string,
            'sub': sub
        })

@login_required
def register_subjects_detail(request,id):
    sub = get_object_or_404(Subscribers, uid=request.user)
    if request.method == 'GET' :
        selected = []
        subject = Subjects.objects.get(pk=id)
        time_fit = []
        now = datetime.date.today()
        for s in subject.time.all():
            if s.end_date > now:
                time_fit.append(s)
        times = subject.time.all()
        tkb = get_object_or_404(TKB,user=request.user)
        for i in tkb.schedule_learn.all():
            for time1 in times:
                if i.time == time1 and i.subject == subject:
                    selected.append(i)
        return render(request,'register_subjects/register_subjects_detail.html',{
            'time':subject, 
            'selected': selected,
            'sub': sub,
            'now': time_fit
        })
@login_required
def create_time_table(request,id, idTime):
    if request.method == 'GET':
        test=''
        sub = Subjects.objects.get(pk=id)
        time = TimeSubjects.objects.get(pk=idTime)
        subscriber = get_object_or_404(Subscribers,uid=request.user) 
        shc=''
        if ScheduleLearn.objects.filter(subject=sub,time=time).exists() :
            shc = ScheduleLearn.objects.get(subject=sub,time=time)
            shc.student.add(subscriber)
            shc.save()
        else: 
            shc = ScheduleLearn.objects.create(
                subject=sub,
                time= time,
            )
            shc.student.add(subscriber)
            shc.save()

        tkb = get_object_or_404(TKB,user=request.user)
        for i in tkb.schedule_learn.all():
            if i.subject == sub or i.time == time:
                shc.student.remove(subscriber)
                shc.save()
                test = 'OK'
                messages.error(request, 'Lịch bị trùng.')
        if test == '':     
            tkb.schedule_learn.add(shc)
            messages.success(request, 'Bạn đã đăng kí thành công !') 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def exit_time_table(request,id):
    sub = Subjects.objects.get(pk=id)
    time = sub.time.all()
    tkb = get_object_or_404(TKB,user=request.user)
    subscriber = get_object_or_404(Subscribers,uid=request.user)
    for i in tkb.schedule_learn.all():
        for time1 in time:
            if i.time == time1 and i.subject == sub:
                tkb.schedule_learn.remove(i)
                i.student.remove(subscriber)
    messages.success(request, 'Huỷ lịch thành công!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
@login_required
def view_time_table(request):
    sub = get_object_or_404(Subscribers, uid=request.user)
    if request.method == 'GET':
        from django.db.models import Count
        tkb = get_object_or_404(TKB, user=request.user)
        schl = tkb.schedule_learn.all().order_by('time__time', 'time__day_of_week')
        schl_test = []
        now = time.localtime()
        for i in schl:
            schl_test.append(
                {
                    "time": i.time.get_time_display(),
                    "date": i.time.day_of_week,
                    "subject": i.subject.name,
                    "teacher": i.time.teacher.all(),
                    "room": i.time.room.all()
                }
            )
        thu = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật']
        return render(request,'tkb/time_table.html',{
            'schl': schl,
            'thu': thu,
            'schl_test': schl_test,
            'sub': sub
        })

def view_tkb(request):
    if request.method == 'GET':
        form = FilterTKBForm(request.GET)
        if form.is_valid():
            query_string=request.GET.get('paradigm')
            if query_string == 'TKB theo tuần':
                return HttpResponseRedirect('/frontend/view-time-table')
            else:
                return HttpResponseRedirect('/frontend/view-tkb-list-subjects')
        else:
            form = FilterTKBForm(
                initial= {
                    'paradigm': 'TKB theo tuần'
                }
            )

def tkb_list_subjects(request):
    sub = get_object_or_404(Subscribers, uid=request.user)
    tkb = get_object_or_404(TKB,user=request.user)
    scheldules = tkb.schedule_learn.all()
    return render(request,'tkb/tkb_list_subjects.html',{
            'schedules': scheldules,
            'sub': sub
        })

def view_students_list(request,id):
    sub = get_object_or_404(Subscribers, uid=request.user)
    schedule = get_object_or_404(ScheduleLearn, id=id)
    students = students = schedule.student.all().order_by('name')
    filters = ['Học viên theo tên', 'Học viên theo ID', 'Học viên theo ngày sinh']
    query_string = 'Học viên theo tên'
    if request.method == 'GET':
        form = FilterTKBForm(request.GET)
        if form.is_valid():
            query_string=request.GET.get('paradigm')
            if query_string == 'Học viên theo tên':
                students = schedule.student.all().order_by('name')
            elif query_string == 'Học viên theo ID':
                students = schedule.student.all().order_by('pk')
            else:
                students = schedule.student.all().order_by('birthday')
        else:
            form = FilterTKBForm(
                initial= {
                    'paradigm': 'Học viên theo tên'
                }
            )
        return render(request, 'tkb/view_students_list.html', {
            'students': students, 
            'sub':sub, 
            'id': schedule.id,
            'filter': filters,
            'query_string': query_string
            })

def download_students_list(view, id):
    schedule = get_object_or_404(ScheduleLearn, id=id)
    students = schedule.student.all().order_by('name')
    i = 1
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DSHV.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['STT', 'ID Học viên', 'Họ và tên', 'Ngày sinh', 'Số điện thoại', 'Email', 'Ghi chú'])
    for student in students:
        writer.writerow([i, student.pk, student.name, student.birthday.strftime('%d-%m-%Y')])
        i = i + 1
    return response