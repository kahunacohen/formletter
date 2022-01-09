from django.contrib import admin
from .models import Letter, Template

class TemplateAdmin(admin.ModelAdmin):
    fields = ['title', 'text',]

admin.site.register(Template, TemplateAdmin)

class LetterAdmin(admin.ModelAdmin):
    fields = ['title', 'template',]

admin.site.register(Letter, LetterAdmin)