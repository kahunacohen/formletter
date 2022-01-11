from django.contrib import admin
from .models import Diagnosis, Letter, Patient, Template

class TemplateAdmin(admin.ModelAdmin):
    fields = ['title', 'text',]

admin.site.register(Template, TemplateAdmin)

class LetterAdmin(admin.ModelAdmin):
    fields = [ 'title', 'template', 'patient']

admin.site.register(Letter, LetterAdmin)

class PatientAdmin(admin.ModelAdmin):
    fields = ['last_4', 'last_initial', 'first_initial', 'diagnoses']

admin.site.register(Patient, PatientAdmin)

class DiagnosisAdmin(admin.ModelAdmin):
    fields = ['name', 'description',]

admin.site.register(Diagnosis, DiagnosisAdmin)