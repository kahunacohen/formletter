from django.db import models

class Template(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  text = models.TextField(max_length=10000)

  def __str__(self):
    return self.title

class Diagnosis(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=1000, null=True, blank=True)
  def __str__(self):
    return self.name

class Patient(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  last_initial = models.CharField(max_length=1)
  first_initial = models.CharField(max_length=1)
  last_4 = models.CharField(max_length=4)
  diagnoses = models.ManyToManyField(Diagnosis)

  def __str__(self):
    return f'{self.last_initial}{self.first_initial}{self.last_4}'

class Letter(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name="template")
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
  

  def __str__(self):
    return self.title
