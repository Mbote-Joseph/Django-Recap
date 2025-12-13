from django import forms
from .models import Books 

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must contain only digits.")
        if len(isbn) not in [10, 13]:
            raise forms.ValidationError("ISBN must be either 10 or 13 digits long.")
        return isbn
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title
    
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if len(author) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long.")
        return author
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        
        if title and author:
            if Books.objects.filter(title=title, author=author).exists():
                raise forms.ValidationError("A book with this title and author already exists.")
        return cleaned_data