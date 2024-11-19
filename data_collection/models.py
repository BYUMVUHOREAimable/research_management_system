# data_collection/models.py
from django.db import models

class Researcher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class ResearchProject(models.Model):
    title = models.CharField(max_length=255)
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.title
