from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    original_air_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
