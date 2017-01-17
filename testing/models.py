from django.core import urlresolvers
from django.db import models
from django.db.models import Min, Max
from unidecode import unidecode
from django.template.defaultfilters import slugify


class Course(models.Model):
    class Meta:
        db_table = "courses"
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    courseName = models.CharField("Название курса", max_length=255, )
    slug = models.SlugField("Отображение в UrL", max_length=50, unique=False, blank=False)
    about=models.TextField("О курсе")

    def questions_course(self):
        list_question = self.question_set.all()
        return list_question

    def save(self):
        super(Course, self).save()
        self.slug = str(self.id) + '_' + slugify(unidecode(self.courseName))
        super(Course, self).save()

    def changeform_link(self):
        if self.id:
            # Replace "myapp" with the name of the app containing
            # your Certificate model:
            changeform_url = urlresolvers.reverse(
                'admin:testing_question_add', args=(self.id,)
            )
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''

    changeform_link.allow_tags = True
    changeform_link.short_description = ''  # omit column header

    def __str__(self):
        return self.courseName


class Question(models.Model):
    class Meta:
        db_table = "questions"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    questionText = models.TextField("Вопрос")
    curse = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def course_question(self):
        course_question = self.curse
        return course_question

    def get_next_question_id(course, question_cur_id):
        if question_cur_id == 0:
            next_question = Course.questions_course(course).aggregate(Min('id'))
            question_id = int(next_question["id__min"])
            return question_id
        else:
            for question in Course.questions_course(course):
                question_id = question.id
                if int(question_id) > int(question_cur_id):
                    question_id = question.id
                    return question_id
                if question_id == Course.questions_course(course).aggregate(Max('id'))["id__max"]:
                    question_id = None
                    return question_id

    def changeform_link(self):
        if self.id:
            # Replace "myapp" with the name of the app containing
            # your Certificate model:
            changeform_url = urlresolvers.reverse(
                'admin:testing_code_question_change', args=(self.id,)
            )
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''

    changeform_link.allow_tags = True
    changeform_link.short_description = ''  # omit column header

    def __str__(self):
        return self.questionText


class Answer(models.Model):
    class Meta:
        db_table = "answers"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    answerText = models.TextField("Текст ответа")
    is_correct = models.BooleanField("Ответ правильный", default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Относиться к вопросу")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Относиться к курсу")

    def __str__(self):
        return self.answerText

    def answers_in_question(self):
        answers_in_question = Question(id=self).answer_set.all()
        return answers_in_question

# Create your models here.