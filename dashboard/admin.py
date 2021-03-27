from django.contrib import admin

# Register your models here.
from dashboard.models import Classroom, School

admin.site.register(School)

@admin.register(Classroom)
class ClassroomId(admin.ModelAdmin):
    list_display = ["name","school"]
    class Meta:
        model=Classroom