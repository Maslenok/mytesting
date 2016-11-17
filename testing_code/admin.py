from django.contrib import admin
from .models import Course, Test, Question, Answer

#class CourseAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("course_name",)}

admin.site.register(Course)
admin.site.register(Test)

# Register your models here.
