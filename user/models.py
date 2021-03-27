from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    ROLE = ((None, "Role"), ('mudur', 'Müdür'), ('ogretmen', 'Öğretmen'),('ogrenci',"Ogrenci"))
    user=models.OneToOneField(User,related_name="profile",verbose_name="User",on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE, blank=False, max_length=10, verbose_name='Görev')
    school=models.ForeignKey("dashboard.School",verbose_name="Okul",related_name="profiles",on_delete=models.CASCADE)

    # eğer rol müdür ise "sınıf" null olacak
    classroom=models.ForeignKey("dashboard.Classroom",verbose_name="Sınıf",related_name="profiles",
                                null=True,blank=True,on_delete=models.CASCADE)
    # @classmethod
    # def create_user(cls,username,email,role,password,school,classroom=None):
    #     user=User.objects.create_user(username,email,password)
    #     cls.objects.create(user=user,role=role,school=school,classroom=classroom)
    #
    #     return user





