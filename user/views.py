from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, update_session_auth_hash, logout as logout_user

# Create your views here.
from dashboard.models import School, Classroom
from user.decorators import anonymous_required
from user.forms import LoginForm, RegisterForm
from user.models import Profile

@anonymous_required
def login(request):

    form=LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login_user(request, user)
                messages.success(request,
                                 "Başarıyla giriş yaptınız. Hoşgeldiniz {} {}"
                                 .format(user.profile.get_role_display(),
                                         user.get_full_name()))
                return redirect("dashboard:index")


    return render(request,"user/login.html",{"form":form})

@anonymous_required
def register(request):
    form=RegisterForm(request.POST or None)

    if  form.is_valid():
        ## Kullanıcı oluştur
        user=form.save(commit=True)

        ## Profil oluştur
        role=request.POST.get("roles")
        school=request.POST.get("school")
        classroom=request.POST.get("classroom")

        Profile.objects.create(user=user,role=role,school_id=school,classroom_id=classroom)

        messages.success(request,"Başarıyla kayıt oldunuz şimdi giriş yapabilirsiniz.")

        return redirect("user:login")
    
    else:print(form.error_messages)

    schools=School.objects.all()

    return render(request,"user/register.html",{"form":form,"schools":schools})

def logout(request):
    logout_user(request)
    messages.success(request, "Başarıyla çıkış yaptınız")
    return redirect("user:login")


def load_clasrooms(request):
    school = request.GET.get('school')
    classrooms = Classroom.objects.filter(school_id=school)

    return render(request, 'includes/classroom_list.html', {'classrooms': classrooms})