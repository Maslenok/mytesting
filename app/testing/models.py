import ckeditor
from django.db import models
from django.db.models import Min, Max
from django.utils.text import slugify
from django.views.generic import ListView
from unidecode import unidecode
from ckeditor.fields import RichTextField


class AboutPage(models.Model):
    class Meta:
        db_table = "about"
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    about=ckeditor.fields.RichTextField(verbose_name=u'Текст')
    title=models.CharField("Заголовок",max_length=100,help_text="О нас")
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)


    def save(self):
        super(AboutPage, self).save()
        self.slug = slugify(unidecode(self.title))
        super(AboutPage, self).save()



    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class Course(models.Model):
    class Meta:
        db_table = "courses"
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    courseName = models.CharField("Название курса", max_length=255, )
    slug = models.SlugField("Отображение в UrL", max_length=50, unique=False, blank=False)
    about=models.TextField("Описание курса ", blank=True)


    def questions_course(self):
        list_question = self.question_set.all()
        return list_question

    def question_len(self):
        course_Len= self.question_set.all().count()
        return course_Len
    question_len.allow_tags= True
    question_len.short_description= "Количество вопросов"

    def save(self):
        super(Course, self).save()
        self.slug = str(self.id) + '_' + slugify(unidecode(self.courseName))
        super(Course, self).save()

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
    course_question.allow_tags= True
    course_question.short_description= "Название курса"

    def get_next_question_id(course, question_cur_id):
        if question_cur_id == 0:
            next_question = Course.questions_course(course).aggregate(Min('id'))
            if next_question["id__min"]:
                question_id = int(next_question["id__min"])
            else:
                question_id= None
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

    def answers_question(self):
        list_answer = self.answer_set.all()
        return list_answer
   # answers_question.allow_tags= True
    #answers_question.short_description= "Ответы на вопрос"

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


