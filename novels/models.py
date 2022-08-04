from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from categories.models import Category

class Novel(models.Model):
    STATUSES = (
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Dropped', 'Dropped'),
    )
    novel_title = models.CharField(max_length=100, verbose_name='Title')
    novel_author = models.CharField(max_length=80, verbose_name='Author')
    novel_categories = models.ManyToManyField(Category)
    novel_status = models.CharField(max_length=9, choices=STATUSES, blank=True, null=True, verbose_name='Status')
    novel_updated = models.DateTimeField(default=timezone.now, verbose_name='Last Updated')
    novel_visible = models.BooleanField(default=False, verbose_name='Visible')

    def __str__(self):
        return self.novel_title






