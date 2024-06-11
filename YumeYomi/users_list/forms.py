from django import forms
from .models import Word, WordList, Tag

class WordListForm(forms.ModelForm):
    class Meta:
        model = WordList
        fields = ['title', 'description', 'date_posted']
    

class WordForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Word
        fields = ['kanji', 'kana', 'romanji', 'meaning', 'usage_example']

    def clean_tags(self):
        tag_names = self.cleaned_data.get('tags')

        return [tag.strip() for tag in tag_names.split(',') if tag.strip()]#split input tags to individual elements

    def save(self, commit=True):
        word = super().save(commit=False)
        tag_names_list = self.cleaned_data.get('tags')

        if commit:
            word.save()  # Save the word instance first
            
            # Create or get existing tags and associate them with the word
            for tag_name in tag_names_list:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                word.tags.add(tag)
        
        return word

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
