from django.db import models

# Create your models here.
class Note(models.Model):
    note = models.TextField(max_length=500)
    title = models.CharField(max_length=50)
    date = models.DateTimeField((), auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.note}, ({self.date})"
