from django.shortcuts import render
from .models import Patient
from django.shortcuts import get_object_or_404

def IntakeView(request, patient_id):
  p = get_object_or_404(Patient, pk=patient_id)
  print(p.diagnoses.all())
  return render(request, 'formletter/intake.html', {'first_initial': p.first_initial, 'last_initial': p.last_initial, 'last_4': p.last_4, 'diagnoses': p.diagnoses.all()})