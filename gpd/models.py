from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BonusPackage(models.Model):
    bonus_name = models.CharField(max_length=30, default='Package ')
    individual_component_weight = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],default='')
    team_component_weight = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],default='')
    CU_component_weight = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],default='')
    complementary_component_weight = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],default='')

    def __str__(self):
        return self.bonus_name 



class Person(models.Model):
    CATEGORY = (
			('Active', 'Active'),
			('Deactivated', 'Deactivated'),
			) 

    name = models.CharField(max_length=30,default='')
    lastname = models.CharField(max_length=30, default='')
    department = models.CharField(max_length=30, default='')
    end_user = models.CharField(max_length=7, default='')
    mng_end_user = models.CharField(max_length=7, default='')
    position = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=200, null=True, choices=CATEGORY)
    bonus_group= models.ForeignKey(BonusPackage, on_delete=models.DO_NOTHING,default='')
    
    

    def __str__(self):
        return self.name +' '+self.lastname+' '+ self.end_user



    

class TableAdmin(admin.ModelAdmin):
    list_display= ('name','lastname', 'end_user','mng_end_user','position','email', 'status','bonus_group')


class Meta:
        verbose_name="Bosch Rexroth GPD Assessment"

class BonusAdmin(admin.ModelAdmin):
    list_display= ('bonus_name','individual_component_weight','team_component_weight','CU_component_weight','complementary_component_weight')

