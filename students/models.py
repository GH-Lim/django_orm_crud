from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
