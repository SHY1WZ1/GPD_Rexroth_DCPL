from django.contrib import admin
from .models import Person, TableAdmin
from django.utils.translation import ugettext_lazy
# Register your models here.


admin.site.register(Person,TableAdmin)
admin.site.site_header = 'Bosch Rexroth administration'
admin.site.index_title = 'GPD administration'
