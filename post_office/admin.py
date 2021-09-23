from django.contrib import admin

# Register your models here.
from .models import Passport


class PassportAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'birthday')


admin.site.register(Passport, PassportAdmin)
