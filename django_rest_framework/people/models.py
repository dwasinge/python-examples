from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return f'{first_name} {last_name} is {age} years old.'