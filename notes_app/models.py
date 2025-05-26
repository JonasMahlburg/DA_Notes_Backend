from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.TextField(max_length=500)
    title = models.CharField(max_length=50)
    date = models.DateTimeField((), auto_now=False, auto_now_add=True)
    marked = models.BooleanField(default=False)
    trash =  models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.note}, ({self.date})"
