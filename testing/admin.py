from django.contrib import admin
from .models import Question, Course, Answer

from django import forms
from .form import QuestionAdminForm,  CourseAdminForm


class AnswerOrderInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        # get forms that actually have valid data
        count_is_correct = 0
        count_is_answers = 0

        for form in self.forms:
            try:
                if form.cleaned_data:
                    count_is_answers +=1
                    if form.cleaned_data.get("is_correct"):
                        count_is_correct +=1
            except AttributeError:
                    # annoyingly, if a subform is invalid Django explicity raises
                    # an AttributeError for cleaned_data
                 pass

        if count_is_answers < 2 :
            raise forms.ValidationError('Должно быть как минимум 2 ответа , и один из них корректный')

        elif  count_is_correct ==0:
            raise forms.ValidationError("Должен быть отмечен хоть один ответ")

        elif count_is_correct == count_is_answers:
            raise forms.ValidationError("Все ответы не могут быть корректными" )





class AnswerInlines(admin.TabularInline):
    model = Answer
    extra = 2
    formset= AnswerOrderInlineFormset

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlines,]
    model = Question
    form = QuestionAdminForm


admin.site.register(Question, QuestionAdmin)


class QuestionInlines(admin.TabularInline):
    model = Question
    show_change_link = True
    extra = 3
    fields = ("questionText", "curse", )
    readonly_fields = ('questionText', )


class CourseAdmin(admin.ModelAdmin):
     inlines = [QuestionInlines,]
     fields = (("courseName", "save_course_link","add_question_link"),)
     readonly_fields = ("add_question_link","save_course_link",)
# list_display = ("courseName","slug", )

admin.site.register(Course, CourseAdmin)