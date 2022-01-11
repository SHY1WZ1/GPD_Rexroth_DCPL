from django.db import models
from django.contrib import admin

# Create your models here.




class Person(models.Model):
    CATEGORY = (
			('Active', 'Active'),
			('Deactivated', 'Deactivated'),
			) 
   # PACKAGE = (
			#('1', '1'),
			#('2', '2'),
   #         ('1/2', '1/2'),
   #         ('K2', 'K2'),
   #         ('3', '3'),
   #         ('K3', 'K3'),
			#) 
    name = models.CharField(max_length=30,default='')
    lastname = models.CharField(max_length=30, default='')
    department = models.CharField(max_length=30, default='')
    end_user = models.CharField(max_length=7, default='')
    mng_end_user = models.CharField(max_length=7, default='')
    position = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=200, null=True, choices=CATEGORY)
    
    

    def __str__(self):
        return self.name +' '+self.lastname+' '+ self.end_user



    

class TableAdmin(admin.ModelAdmin):
    list_display= ('name','lastname', 'end_user','mng_end_user','position','email', 'status')


class Meta:
        verbose_name="Bosch Rexroth GPD Assessment"

class BonusAdmin(admin.ModelAdmin):
    list_display= ('bonus_group_name','individual_comp_weight')

