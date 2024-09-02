from django import forms
from .models import bookModel, author


class BookForm(forms.ModelForm):
    author_name = forms.CharField(max_length=255, label='Author Name')

    class Meta:
        model = bookModel
        fields = ['title', 'price', 'publication_date','author']

    def save(self, commit=True):
        book = super().save(commit=False)
        author_name = self.cleaned_data['author_name']
        Author, created = author.objects.get_or_create(name=author_name)
        book.Author = Author
        if commit:
            book.save()
        return book
