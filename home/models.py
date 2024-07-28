from django.db import models

# Create your models here.
class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.ImageField(upload_to="sample_model_images")