from django.shortcuts import render

def IntakeView(request):
  return render(request, 'formletter/intake.html', {'diagnoses': ['foo', 'bar']})