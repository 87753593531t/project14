from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='name')
    surname = models.CharField(max_length=50, default='', verbose_name='surname')
    city = models.CharField(max_length=50, default='', verbose_name='city')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return str(self.id)
