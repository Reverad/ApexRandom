from django.db import models


# Create your models here.
class Legend(models.Model):
    name = models.CharField(max_length=100)
    class_type = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.CharField(max_length=250, default="No description yet")

    def __str__(self):
        return self.name
