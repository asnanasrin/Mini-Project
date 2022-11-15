from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(regmodel)
admin.site.register(casemodel)
admin.site.register(rulemodel)
admin.site.register(usermodel)
admin.site.register(resultmodel)
