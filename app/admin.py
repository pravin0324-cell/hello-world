from django.contrib import admin
from .models import School
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

admin.site.register(School, SchoolAdmin)    