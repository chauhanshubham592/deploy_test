from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.title}"