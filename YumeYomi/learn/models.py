from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Radicals(models.Model):
    radical_id = models.PositiveIntegerField(primary_key=True)
    radical = models.CharField(max_length=1, unique=True, verbose_name="Radical Character")
    other_forms = models.CharField(max_length=50, blank=True, verbose_name="Other Forms")
    radical_meaning = models.CharField(max_length=100, verbose_name="Meaning")
    radical_stroke_count = models.PositiveIntegerField(verbose_name="Stroke Count")
    reading_hiragana = models.CharField(max_length=100, blank=False, default='', verbose_name="Hiragana Reading")
    reading_romanji = models.CharField(max_length=100, blank=False, default='', verbose_name="Romanji Reading")

    class Meta:
        verbose_name = "Radical"
        verbose_name_plural = "Radicals"
        ordering = ['radical_id']

    def __str__(self):
        return f"{self.radical} ({self.radical_meaning})"

