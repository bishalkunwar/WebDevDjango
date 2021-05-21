from django.contrib import admin
from .models import ( mails )

# Register your models here.

@admin.register(mails)
class mailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'c_number', 'message']