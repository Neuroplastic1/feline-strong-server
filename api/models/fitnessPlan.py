from django.db import models

from .user import User

# Create your models here.
class FitnessPlan(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  date = models.CharField(max_length=100)
  plan = models.CharField(max_length=100)
  nutrition = models.CharField(max_length=100)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"date:{self.date} plan:{self.plan} nutrition:{self.nutrition} "

  def as_dict(self):
    """Returns dictionary version of fitnessPlan models"""
    return {
        'id': self.id,
        'date': self.date,
        'plan': self.plan,
        'nutrition': self.nutrition
    }
