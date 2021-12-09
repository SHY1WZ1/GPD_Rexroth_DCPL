from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30,default='')
    surname = models.CharField(max_length=30, default='')
    department = models.CharField(max_length=30, default='')
    NTUser_ID = models.CharField(max_length=30, default='')
    manager=models.CharField(max_length=30)

    def __str__(self):
        return self.name +' '+self.surname


class TableAdmin(admin.ModelAdmin):
    list_display= ('name','surname', 'NTUser_ID','department','manager')


class Meta:
        verbose_name="Bosch Rexroth GPD Assessment"