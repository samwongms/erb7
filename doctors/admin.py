from django.contrib import admin
from .models import Doctor

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('name', 'email')
    search_fields = ('name',)
    list_per_page = 25
    list_editable = ('is_mvp',)
    

admin.site.register(Doctor, DoctorAdmin)

