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


class Radical(models.Model):
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
class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    radicals = models.ManyToManyField(Radical, related_name='characters')
    meaning = models.TextField(blank=True, null=True)
    readings = models.CharField(max_length=255, blank=True, null=True)
    strokes = models.PositiveIntegerField(verbose_name="Stroke Count", null=True, blank=True)
    frequency = models.PositiveIntegerField(verbose_name="Frequency of Use", null=True, blank=True)

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ['name']

    def __str__(self):
        return self.name
    
class CharacterEdit(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='edits')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character_edits')
    new_meaning = models.TextField(blank=True, null=True)
    new_readings = models.CharField(max_length=255, blank=True, null=True)
    new_strokes = models.PositiveIntegerField(null=True, blank=True)
    new_frequency = models.PositiveIntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


    def apply_edit(self):
        """Apply the edit to the character model if approved."""
        if self.approved:
            if self.new_meaning:
                self.character.meaning = self.new_meaning
            if self.new_readings:
                self.character.readings = self.new_readings
            if self.new_strokes:
                self.character.strokes = self.new_strokes
            if self.new_frequency:
                self.character.frequency = self.new_frequency
            self.character.save()

    def delete(self, *args, **kwargs):
        """Delete the edit and check if the character should be also deleted."""
        character = self.character
        super().delete(*args, **kwargs)
        #After deleting, check if there are any edits left for the character
        if not CharacterEdit.objects.filter(character=character).exists():
            character.delete()

    class Meta:
        verbose_name = "Character Edit"
        verbose_name_plural = "Character Edits"
        ordering = ['submitted_at']

    def __str__(self):
        return f"Edits for {self.character.name} by {self.user.username}"