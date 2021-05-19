from django.contrib import admin
from .models import UsernamePasswordService

class password_admin(admin.ModelAdmin):
    list_display = ['service', 'user_name', 'secret']

admin.site.register(UsernamePasswordService, password_admin)
