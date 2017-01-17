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
    about=models.TextField("О курсе", blank=True)

    def questions_course(self):
        list_question = self.question_set.all()
        return list_question

    def save(self):
        super(Course, self).save()
        self.slug = str(self.id) + '_' + slugify(unidecode(self.courseName))
        super(Course, self).save()

    def add_question_link(self):
        if self.id:
            # Replace "myapp" with the name of the app containing
            # your Certificate model:
            changeform_url ="/admin/testing/question/add/"
            return u'<a href="%s" target="_blank">Добавить вопрос</a>' % changeform_url
        return u''

    add_question_link.allow_tags = True
    add_question_link.short_description = ''


    def save_course_link(self):
        changeform_url= "/admin/testing/course/save/"
        return u'<a href="%s" target="_blank">Сохранить курс</a>' % changeform_url

    save_course_link.allow_tags = True
    save_course_link.short_description = ''

    # omit column header

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


    def __str__(self):
        return self.answerText

    def answers_in_question(self):
        answers_in_question = Question(id=self).answer_set.all()
        return answers_in_question

# Create your models here.
