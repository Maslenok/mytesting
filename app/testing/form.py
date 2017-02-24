from django import forms
from django.forms.models import modelformset_factory, modelform_factory
from .models import Course, Question

#AnswerAdminFormSet= modelform_factory(AboutPage, fields=("about", "is_active", "position",))

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("questionText","curse",)

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("courseName","slug", "about")



