from django.db import models
from django.contrib.auth.models import User
from testing_code.models import Question,Course, Answer

class Result(models.Model):
    class Meta:
        db_table="result"

    date_created=models.DateTimeField('date published')
    is_complete=models.BooleanField(default= False)
    result_value=models.IntegerField(default=0)
    users=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)



class UsersAnswer(models.Model):
    class Meta:
        db_table="usersAnswers"

    users=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answers_list=models.TextField()
    result=models.ForeignKey(Result, on_delete=models.CASCADE)


