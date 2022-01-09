from django.db import models

class Template(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100)
  text = models.TextField(max_length=10000)

  def __str__(self):
    return self.title