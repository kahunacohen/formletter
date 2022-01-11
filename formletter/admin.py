from django.contrib import admin
from .models import Diagnosis, Letter, Patient, LetterType

class LetterTypeAdmin(admin.ModelAdmin):
    fields = ['type',]

admin.site.register(LetterType, LetterTypeAdmin)

class LetterAdmin(admin.ModelAdmin):
    fields = [ 'title', 'type', 'patient']

admin.site.register(Letter, LetterAdmin)

class PatientAdmin(admin.ModelAdmin):
    fields = ['last_4', 'last_initial', 'first_initial', 'diagnoses']

admin.site.register(Patient, PatientAdmin)

class DiagnosisAdmin(admin.ModelAdmin):
    fields = ['name', 'description',]

admin.site.register(Diagnosis, DiagnosisAdmin)