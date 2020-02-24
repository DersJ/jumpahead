from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(null=True)


class Module(models.Model):
    video_link = models.URLField(max_length=250, blank=True)
    title = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    course = models.ForeignKey("Course",
                               on_delete=models.CASCADE,
                               related_name="modules")


class Task(models.Model):
    module = models.ForeignKey("modules.Module",
                               on_delete=models.CASCADE,
                               related_name="tasks")
    description = models.TextField()