from django.db import models

# Create your models here.
class Email(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  time = models.DateField()
  status = models.BooleanField(default=False)

  def __str__(self):
    return self.title
