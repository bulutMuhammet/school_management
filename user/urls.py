from django.urls import path
from user import views

app_name = "user"

urlpatterns=[
    path("giris-yap/",views.login,name="login"),
    path("kayit-ol/",views.register,name="register"),
    path("cikis-yap/",views.logout,name="logout"),

    path('/siniflari-getir/', views.load_clasrooms, name='load_clasrooms'),

]