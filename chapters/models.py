from django.db import models
from novels.models import *

class Chapter(models.Model):
    chapter_number = models.IntegerField(verbose_name='Numero')
    chapter_novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='Novel')
    chapter_title = models.CharField(max_length=80, verbose_name='Titulo')
    chapter_content = models.TextField()
    chapter_visible = models.BooleanField(default=False)

    def __str__(self):
        return f'Chapter {self.chapter_number}'
