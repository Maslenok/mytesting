from django import forms
from django.forms.models import modelformset_factory, modelform_factory
from .models import Course, Answer, Question, AboutPage

AnswerAdminFormSet= modelform_factory(AboutPage, fields=("about", "is_active"))

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("questionText","curse",)

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("courseName","slug", "about")



