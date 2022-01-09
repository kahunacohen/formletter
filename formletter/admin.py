from django.contrib import admin
from .models import Template

class TemplateAdmin(admin.ModelAdmin):
    fields = ['title', 'text',]

admin.site.register(Template, TemplateAdmin)