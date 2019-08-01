from django.db import models

# Create your models here.


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)

    def __str__(self):
        self.cname


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=16)

    cid = models.ForeignKey(to="Class",to_field="id",related_name="students",on_delete=models.CASCADE)
    detail = models.OneToOneField("StudentDetail",null=True,on_delete=models.CASCADE)


class StudentDetail(models.Model):
    height = models.PositiveIntegerField()
    email = models.EmailField()
    memo = models.CharField(max_length=128,null=True)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField("Class",null=True)

    def __str__(self):
        self.tname

