from django.db import models
from django.db.models import Min, Max
from unidecode import unidecode
from django.template.defaultfilters import slugify



class Course(models.Model):
    class Meta:
        db_table="courses"
        verbose_name= "Курс"
        verbose_name_plural ="Курсы"

    course_name=models.CharField("Название курса" ,max_length=255,)   
    slug = models.SlugField(max_length=50, unique=False, blank=False)

    def questions_course(self):
        list_question=self.question_set.all()
        return list_question

   
    def save(self):     
        super(Course, self).save()
        self.slug = str(self.id) + '_' + slugify(unidecode(self.course_name)) 
        super(Course, self).save() 

    def __str__(self):
        return self.course_name


class Question(models.Model):
    class Meta:
        db_table="questions"

    question_text=models.TextField()
    curse=models.ForeignKey(Course,  on_delete=models.CASCADE)
    
    def course_question(self):
        course_question=self.curse
        return course_question


    def get_next_question_id(course, question_cur_id):
        if question_cur_id==0:
            next_question=Course.questions_course(course).aggregate(Min('id'))
            question_id=int(next_question["id__min"])
            return question_id
        else:
            for question in Course.questions_course(course):
                question_id = question.id
                if  int(question_id) > int(question_cur_id):
                    question_id=question.id
                    return question_id
                if question_id == Course.questions_course(course).aggregate(Max('id'))["id__max"] :
                    question_id = None
                    return question_id






    
    def __str__(self):
        return self.question_text

class Answer (models.Model):
    class Meta:
        db_table="answers"

    answer_text=models.TextField()
    is_correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.answer_text

    def answers_in_question(self):
        answers_in_question =Question(id=self).answer_set.all()
        return  answers_in_question




