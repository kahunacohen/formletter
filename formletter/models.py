from django.db import models

class Template(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  text = models.TextField(max_length=10000)

  def __str__(self):
    return self.title

class Letter(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=100)
  template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name="template")
  

  def __str__(self):
    return self.title