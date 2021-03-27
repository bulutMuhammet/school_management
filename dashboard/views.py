
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from dashboard.decorators import role_required
from dashboard.forms import UserUpdateForm, ProfileUpdateForm
from user.models import Profile


@login_required(login_url="user:login")
def index(request):
    return render(request, "dashboard/index.html")


@login_required(login_url="user:login")
def edit_profile(request):
    u_form = UserUpdateForm(request.user, request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.user,request.POST or None, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save(commit=True)
        p_form.save(commit=True)
        messages.success(request, "Bilgiler başarıyla değiştirildi.")

        return redirect("dashboard:index")

    return render(request, "dashboard/edit_profile.html", {"u_form": u_form, "p_form": p_form})


@login_required(login_url="user:login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parolanız başarıyla değiştirildi')
            return redirect('dashboard:index')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {'form': form})


@login_required(login_url="user:login")
@role_required(["mudur"])
def teachers(request):
    teachers = Profile.objects.filter(role="ogretmen",school_id=request.user.profile.school.id)
    return render(request, "dashboard/teachers.html", {"teachers": teachers})


@login_required(login_url="user:login")
@role_required(["mudur"])
def edit_teacher(request, username):
    teacher = Profile.objects.get(user__username=username)
    u_form = UserUpdateForm(teacher.user, request.POST or None, instance=teacher.user)
    p_form = ProfileUpdateForm(teacher.user,request.POST or None, instance=teacher)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save(commit=True)
        p_form.save(commit=True)
        messages.success(request, "{} kullanıcısının bilgileri başarıyla değiştirildi.".format(teacher.user))

        return redirect("dashboard:teachers")

    return render(request, "dashboard/edit_teacher.html", {"u_form": u_form, "p_form": p_form})


@login_required(login_url="user:login")
@role_required(["mudur", "ogretmen"])
def students(request):
    students = Profile.objects.filter(role="ogrenci",school_id=request.user.profile.school.id)
    return render(request, "dashboard/students.html", {"students": students})


@login_required(login_url="user:login")
@role_required(["mudur", "ogretmen"])
def edit_student(request, username):
    student = Profile.objects.get(user__username=username)
    u_form = UserUpdateForm(student.user, request.POST or None, instance=student.user)
    p_form = ProfileUpdateForm(student.user,request.POST or None, instance=student)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save(commit=True)
        p_form.save(commit=True)
        messages.success(request, "{} kullanıcısının bilgileri başarıyla değiştirildi.".format(student.user))

        return redirect("dashboard:students")

    return render(request, "dashboard/edit_teacher.html", {"u_form": u_form, "p_form": p_form})
