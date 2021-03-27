from django import forms
from django.contrib.auth.models import User

from dashboard.models import Classroom
from user.models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def __init__(self,user, *args, **kwargs):
        self.user = user
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Tüm alanlara form-control classını ekle
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    # Eposta sistemde kayıtlı mı kontrol et
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if User.objects.filter(email=email).exists():
            if email != self.user.email:
                raise forms.ValidationError('Bu e-posta sistemde kayıtlı')
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'school', 'classroom']

    def __init__(self,user, *args, **kwargs):
        self.user=user
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # Tüm alanlara form-control classını ekle
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        if self.user.profile.role=="mudur":
            self.fields["classroom"].widget=forms.HiddenInput()

