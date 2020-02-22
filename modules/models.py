from django.db import models

# Create your models here.
class Module(models.Model):
    video_link = models.URLField(max_length=250, blank=True)
    title = models.CharField(max_length=500)
    created = models.DateField(auto_now=False, auto_now_add=True)
    last_updated = models.DateField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    task_list = models.ForeignKey('TaskList', on_delete=models.CASCADE, blank=True, null=True)

class TaskList(models.Model):
    sample = models.CharField(max_length=200)
