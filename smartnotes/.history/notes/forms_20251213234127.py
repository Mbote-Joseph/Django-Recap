from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text', 'likes')
        Widgets = {
            'text': forms.Textarea(attrs={"class": "form-control my-5", 'rows':4, 'cols':15}),
            'title': forms.TextInput(attrs={"class": "form-control my-5", 'placeholder': 'Enter Note Title'}),
        }
        labels = {
            'title': 'Note Title',
            'text': 'Note Content',
            'likes': 'Number of Likes'
        }
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("Content must be at least 10 characters long.")
        return content
    