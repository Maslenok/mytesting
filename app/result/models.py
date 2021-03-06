from django.db import models

#from app.testing import Question,Course
from app.testing.models import Course, Question
from core.models import User


class Result(models.Model):
    class Meta:
        db_table="result"
        verbose_name = "Результат тестирования"
        verbose_name_plural = "Результаты тестирований"
    dateCreated=models.DateTimeField("Дата прохождения",auto_now_add=True)
    is_complete=models.BooleanField("Тест окончен", default= False)
    resultValue=models.IntegerField("Результат",default=0)
    users=models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    course=models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name= "Курс")

    def __str__(self):
      return str(self.users)

class UsersAnswer(models.Model):
    class Meta:
        db_table="usersAnswers"
    users=models.ForeignKey(to=User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    right=models.BooleanField(default= False)
    result=models.ForeignKey(Result, on_delete=models.CASCADE)


    def __str__(self):
        return ("Ответ на вопрос"+"_"+str(self.question))





