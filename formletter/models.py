from django.db import models


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

class LetterType(models.Model):
  type = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.type

class Letter(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  type = models.ForeignKey(LetterType, on_delete=models.CASCADE, related_name="letter_type")
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
  

  def __str__(self):
    return self.title
