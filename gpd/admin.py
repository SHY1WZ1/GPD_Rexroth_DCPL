from django.contrib import admin
from .models import Person, TableAdmin
# Register your models here.


admin.site.register(Person,TableAdmin)