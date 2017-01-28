from django.db import models
from django.contrib.auth.models import User
from testing.models import Question,Course, Answer

class Result(models.Model):
    class Meta:
        db_table="result"
        verbose_name = "Результат тестирования"
    dateCreated=models.DateTimeField("Дата прохождения",auto_now_add=True)
    is_complete=models.BooleanField("Посностью окончил",default= False)
    resultValue=models.IntegerField("Результат",default=0)
    users=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    course=models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name= "Курс")

    def __str__(self):
      return str(self.users)

class UsersAnswer(models.Model):
    class Meta:
        db_table="usersAnswers"
    users=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    right=models.BooleanField(default= False)
    result=models.ForeignKey(Result, on_delete=models.CASCADE)


    def __str__(self):
        return (str(self.users)+"_"+str(self.question))





