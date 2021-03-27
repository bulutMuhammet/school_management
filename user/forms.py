import re

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import  forms

from user.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(required=True, max_length=50,widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)
        # Tüm alanlara form-control classını ekle
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Email or password wrong')

    # Email veya kullanıcı adı ile giriş yapılabilir, en sonunda username döner
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            users = User.objects.filter(email__iexact=username)
            if len(users) > 0 and len(users) == 1:
                return users.first().username
        return username

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2', )


    def __init__(self,*args, **kwargs):

        super(RegisterForm, self).__init__(*args, **kwargs)
        # Tüm alanlara form-control classını ekle
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

        self.fields["first_name"].required=True
        self.fields["last_name"].required=True
        self.fields["email"].required=True

    #Eposta sistemde kayıtlı mı kontrol et
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('Bu email zaten kayıtlı.')
        return email

    #Parolalar eşleşiyor mu kontrol et
    def clean_password2(self):
        print("la sorun ne amk")
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Parolanızı onaylamanız gerekmektedir.")
        print(password2,password1)
        if password1 != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        return password2



