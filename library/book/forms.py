from django import forms
from .models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,   # або forms.SelectMultiple
        required=False
    )

    class Meta:
        model = Book
        fields = ["name", "description", "count", "authors"]
