from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_img = models.ImageField(upload_to='media/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.category_name

