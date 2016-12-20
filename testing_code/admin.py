from django.contrib import admin
from .models import Course, Question, Answer

"""

Django-admin-tools

"""

class AnswerInline(admin.TabularInline):
    model = Answer
    show_change_link = True


class QuestioInLine(admin.TabularInline):
    model =Question
    #fields=("AnswerInLine",)
    inlines=[AnswerInline,]
    show_change_link = True


class QuestioAdnmin(admin.ModelAdmin):
    inlines=[AnswerInline, ]
    model= Question
    
    list_display=('question_text', 'curse' ,'course_question',)
    
    

class CourseAdmin(admin.ModelAdmin):           
    inlines=[QuestioInLine,AnswerInline,] 
    
    def course_list(self):
        list=Course.objects.get(course_name='self_name')
        return list
    
    

    list_display=( 'course_name', 'slug')
  #  list_display_links=('slug')
    fieldsets = (
        ("Курсы", {
            'fields': ('course_name',  )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ( ),
        }),
    )
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestioAdnmin)


# Register your models here.
