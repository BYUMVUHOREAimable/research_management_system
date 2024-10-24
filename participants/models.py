from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
