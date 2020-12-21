from .forms import (
    LoginForm,
    RegisterForm,
    CommentForm,
    UpdateProfileForm,
    RegisterSubjectsForm
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


def index(request):
    return render(request,'index.html')
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
                print(form.cleaned_data['email'])
                sub = Subscribers.objects.create(
                    uid=user,
                    name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    birthday= datetime.datetime.now(),
                    phone=form.cleaned_data['phone_number'],
                    position=form.cleaned_data['groups'],
                    current_address='',
                    status=True,
                )
                sub.save()
                print(sub)
                tkb = TKB.objects.create(user=user)
                tkb.save()
                print(tkb)
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/home')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

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
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def password_change(request):
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
        'form': form
    })

def comment(request):
    template = 'comments.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        print(request.POST.get('comment'))
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
    
    if request.method == 'POST' :
        sub = Subscribers.objects.filter(uid=request.user.username)[0]
        form = UpdateProfileForm( request.POST)
        
        if form.is_valid():
            Subscribers.objects.filter(uid=request.user.username).update(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                birthday=request.POST.get('birthday'),
                phone = request.POST.get('phone'),
                current_address= request.POST.get('current_address'),
                position= request.POST.get('position'),
                updated_at= datetime.datetime.now()
            )
            messages.success(request, 'Your profile was successfully update!')
            return redirect('/home')
        else: messages.error(request, 'Please correct the error below.')
   # No post data availabe, let's just show the page.
    else:
        form = UpdateProfileForm()
        sub = Subscribers.objects.filter(uid=request.user)[0]

    return render(request, template, {
        'form': form,
        'sub': sub,
        })

@login_required
def register_subjects(request):
    if request.method == 'GET':
        subj = Subjects.objects.all()
        return render(request,'register_subjects.html',{
            'subj': subj,
        })
@login_required
def register_subjects_detail(request,id):
    if request.method == 'GET' :
        time = Subjects.objects.get(pk=id)
        return render(request,'register_subjects_detail.html',{
            'time':time
        })
@login_required
def create_time_table(request,id, idTime):
    if request.method == 'GET':
        sub = Subjects.objects.get(pk=id)
        time = TimeSubjects.objects.get(pk=idTime)
        shc=''
        if ScheduleLearn.objects.filter(subject=sub,time=time).exists() :
            shc = ScheduleLearn.objects.get(subject=sub,time=time)
            shc.student.add(request.user)
            shc.save()
        else: 
            shc = ScheduleLearn.objects.create(
                subject=sub,
                time= time,
            )
            shc.student.add(request.user)
            shc.save()

        tkb = get_object_or_404(TKB,user=request.user)
        for i in tkb.schedule_learn.all():
            if i.subject == sub:
                return render(request, 'register_subjects_detail.html', {
                    'error_message': 'Lịch bị trùng.'
                })
        tkb.schedule_learn.add(shc)
        messages.success(request, 'Bạn đã đăng kí thành công !')
        return render(request, 'register_subjects_detail.html', {
                'message': 'Bạn đã đăng kí thành công !'
            })
    return redirect('/frontend/register-subjects-detail/')

@login_required
def exit_time_table(request,id):
    if request.method == 'GET':
        sub = Subjects.objects.get(pk=id)
        student= request.user
        if ScheduleLearn.objects.filter(subject=sub, student=student).delete() :
            return render(request, 'register_subjects_detail.html', {
                    'success_message': 'Huỷ lịch thành công!'
                })
    return redirect('/frontend/register-subjects-detail/')

@login_required
def view_time_table(request):
    print(get_object_or_404(TKB, user=request.user))
    if request.method == 'GET':
        tkb = get_object_or_404(TKB, user=request.user)
        schl = tkb.schedule_learn.all().order_by('time')
        thu = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật']
        return render(request,'time_table.html',{
            'schl': schl,
            'thu': thu,
        })
