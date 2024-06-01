from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class WordList(models.Model):
    PRIVACY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='public')


    def __str__(self):
        return self.title
    
    def entry_count(self):
        return self.words.count()
    
    def count_likes(self):
        return self.likes.count()

    def user_already_liked(self, user):
        return self.likes.filter(user=user).exists()

    
class Word(models.Model):
    word_list = models.ForeignKey(WordList, related_name='words', on_delete=models.CASCADE)
    kanji = models.CharField(max_length=255, blank=True)
    kana = models.CharField(max_length=255)
    romanji = models.CharField(max_length=255)
    meaning = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.kana


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_list = models.ForeignKey(WordList, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'word_list']