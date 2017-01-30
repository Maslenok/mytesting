from django.contrib import admin
from .models import Question, Course, Answer, AboutPage
from django import forms


class AnswerOrderInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
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
    inlines = [AnswerInlines, ]
    show_change_link = True
    list_display = ("questionText","course_question", )
    fields = ("questionText", "curse")
    list_filter=["curse",]
    list_per_page=10

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'curse' and request.GET.get("course"):
            kwargs['queryset'] = Course.objects.filter(id=request.GET.get("course"))
            return db_field.formfield(**kwargs)
        return super(QuestionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if request.GET.get("course"):
           extra_context['add_question'] = True
           extra_context['id_course']= request.GET.get("course")
           extra_context["curse"]= Course.objects.get(id=request.GET.get("course"))
        return self.changeform_view(request, None, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['question'] = Question.objects.get(id=object_id)
        return self.changeform_view(request, object_id, form_url, extra_context)

class QuestionInlines(admin.TabularInline):
    model = Question
    show_change_link = True
    extra = 3
    fields = ("questionText", "curse", )
    readonly_fields = ('questionText', )

class CourseAdmin(admin.ModelAdmin):
     inlines = [QuestionInlines,]
     fields = ("courseName", "about")
     list_display = ("courseName", "question_len")

     def add_view(self, request, form_url='', extra_context=None):
         extra_context = extra_context or {}
         extra_context['add_batton'] = False

         return self.changeform_view(request, None, form_url, extra_context)

     def change_view(self, request, object_id, form_url='', extra_context=None):
         extra_context = extra_context or {}
         extra_context['add_batton'] = True
         extra_context['course_id'] = object_id
         return self.changeform_view(request, object_id, form_url, extra_context)

class AboutPageAdmin(admin.ModelAdmin):
    show_change_link = True
    list_display = ("about", "is_active",)
    fields = ("about", )
    ordering = ["-is_active",]
    list_editable=("is_active",)


admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Course, CourseAdmin)
