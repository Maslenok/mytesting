from django.db import models


class Course(models.Model):
    class Meta:
        db_table="courses"

    course_name=models.CharField(max_length=255)
    url=models.URLField("URL")

    def __str__(self):
        return self.course_name


class Test(models.Model):
    class Meta:
        db_table="tests"

    test_name=models.CharField(max_length=255)
    curse=models.ForeignKey(Course,  on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name

class Question(models.Model):
    class Meta:
        db_table="questions"

    question_text=models.TextField()
    test=models.ForeignKey(Test , on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Answer (models.Model):
    class Meta:
        db_table="answers"

    answer_text=models.TextField()
    is_correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text



