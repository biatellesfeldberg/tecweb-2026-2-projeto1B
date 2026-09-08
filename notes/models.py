from django.db import models

# Create your models here
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.id}. {self.name}"

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}. {self.title}"
