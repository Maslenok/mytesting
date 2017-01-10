from django import forms
from django.forms.models import modelformset_factory
from .models import Course, Answer, Question


class AnswerAdminForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("answer_text","is_correct",)


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_text","curse",)


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("course_name",)



