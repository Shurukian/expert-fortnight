from django.db import models
from django.contrib.auth import get_user_model

# Create the Flashcard Model
class Flashcard(models.Model):
  # All of the Flashcard Model fields, ref # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  question = models.CharField(max_length=250)
  answer = models.CharField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
)

  def __str__(self):
    return self.title

  def as_dict(self):
    """This will return a dictionary of the Flashcard models"""
    return {
        'id': self.id,
        'title': self.question,
        'question': self.question,
        'answer': self.answer,
    }
