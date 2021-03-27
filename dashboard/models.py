from django.db import models

# Create your models here.
class School(models.Model):
    CITY = ((None, "Şehir"), ('rize', 'Rize'), ('artvin', 'Artvin'),('trabzon',"Trabzon"))

    name = models.CharField(max_length=200,verbose_name="Okul Adı",null=False,blank=False)
    city = models.CharField(choices=CITY, blank=False, null=False,max_length=10, verbose_name='Şehir')

    class Meta:
        verbose_name="Okul"
        verbose_name_plural="Okullar"

    def __str__(self):
        return self.name

    # okul müdürünu getir
    def get_manager(self):
        return self.profiles.get(role="mudur")

class Classroom(models.Model):
    name = models.CharField(max_length=10,verbose_name="Sınıf Adı",blank=False,null=False)
    school = models.ForeignKey(School,verbose_name="Okul",related_name="classes",on_delete=models.CASCADE)

    class Meta:
        verbose_name="Sınıf"
        verbose_name_plural="Sınıflar"

    def __str__(self):
        return self.name

    # sınıf öğretmenini getir
    def get_teacher(self):
        return self.profiles.get(role="ogretmen")
