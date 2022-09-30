from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    mark = models.IntegerField()
    stu_location = models.CharField(max_length=25)

    def __str__(self):
        return self.name
