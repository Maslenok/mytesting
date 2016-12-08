from django.db import models
from unittest.util import _MAX_LENGTH
from unidecode import unidecode
from django.template.defaultfilters import slugify



class Course(models.Model):
    class Meta:
        db_table="courses"
        verbose_name= "Курс"
        verbose_name_plural ="Курсы"

    course_name=models.CharField("Название курса" ,max_length=255,)   
    slug = models.SlugField(max_length=50, unique=False, blank=False)

    def question_course(self): 
              
       # course_question=Course.objects.get(self)
        list_question=self.question_set.all()[:5]
        list=[]
        for qustion in list_question:
            list.append(qustion)
       
        return list
    
    
 #def question_course1(self):
  #       course_question=Question.objects.filter(self)
   #      return course_question

   
    def save(self):     
        super(Course, self).save()
        self.slug = str(self.id) + '_' + slugify(unidecode(self.course_name)) 
        super(Course, self).save() 

    def __str__(self):
        return self.course_name

"""
class Test(models.Model):
    class Meta:
        db_table="tests"

    test_name=models.CharField(max_length=255)
    curse=models.ForeignKey(Course,  on_delete=models.CASCADE , related_query_name="tag")
    

    def __str__(self):
        return self.test_name
"""
class Question(models.Model):
    class Meta:
        db_table="questions"

    question_text=models.TextField()
    curse=models.ForeignKey(Course,  on_delete=models.CASCADE)
    
    def course_question(self):
        course_question=Course.objects.filter(course_name = self.curse)
        #course_question=Course.objects.all()
        return course_question[0]
    
 
    
    # entry__headline__contains
    
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



