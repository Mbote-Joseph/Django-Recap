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