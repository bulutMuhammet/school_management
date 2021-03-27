from django.urls import path
from dashboard import views

app_name = "dashboard"

urlpatterns=[
    path("",views.index,name="index"),
    path("profili-duzenle",views.edit_profile,name="edit_profile"),
    path("parolayi-degistir",views.change_password,name="change_password"),
    path("ogretmenler",views.teachers,name="teachers"),
    path("ogretmen-duzenle/<str:username>",views.edit_teacher,name="edit_teacher"),
    path("ogrenciler",views.students,name="students"),
    path("ogrenci-duzenle/<str:username>", views.edit_student, name="edit_student"),

]