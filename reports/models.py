from django.db import models

class Report(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    report_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.project.title} at {self.created_at}"
