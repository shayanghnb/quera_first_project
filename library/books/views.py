from django.shortcuts import render, get_object_or_404, redirect
from .models import bookModel, author
from .forms import BookForm


def book_list(request):
    books = bookModel.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(bookModel, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(bookModel, pk=pk)
    book.delete()
    return redirect('book_list')


def search_books(request):
    query = request.GET.get('q')
    books = bookModel.objects.filter(title__icontains=query) if query else bookModel.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
