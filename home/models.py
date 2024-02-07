from django.db import models
from django.contrib.auth.models import User
class registration(models.Model):
        user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


class DEPARTMENT(models.Model):
    department=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.department
    class Meta:
        ordering=['department']

class STUDENTID(models.Model):
    student_id=models.TextField(max_length=50)
    def __str__(self) -> str:
        return self.student_id
    class Meta:
        ordering=['student_id']
class SUBJECT(models.Model):
    subject_name=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.subject_name

class STUDENT(models.Model):
    department=models.ForeignKey(DEPARTMENT,on_delete=models.SET_NULL,null=True)
    student_id=models.OneToOneField(STUDENTID,on_delete=models.SET_NULL,null=True)
    student_name=models.CharField(max_length=200)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_addre=models.TextField()
class SUBJECTMARKS(models.Model):
    student=models.ForeignKey(STUDENT,on_delete=models.SET_NULL,null=True,related_name='studentmarks')
    subject=models.ForeignKey(SUBJECT,on_delete=models.SET_NULL,null=True)
    mark=models.IntegerField()
    class Meta:
        unique_together=['student','subject']
