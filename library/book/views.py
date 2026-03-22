from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.shortcuts import render, redirect
from .forms import BookForm
from author.models import Author


# def book_list(request):
#     books = Book.get_all()
#     return render(request, 'books/book_list.html', {'books': books})
def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    name = request.GET.get("name")
    author = request.GET.get("author")
    min_count = request.GET.get("min_count")

    if name:
        books = books.filter(name__icontains=name)

    if author:
        books = books.filter(authors__id=author)

    if min_count:
        books = books.filter(count__gte=min_count)

    return render(request, "books/book_list.html", {
        "books": books,
        "authors": authors,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})



def book_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        count = request.POST.get("count")
        authors_ids = request.POST.getlist("authors")

        book = Book.objects.create(
            name=name,
            description=description,
            count=count
        )

        if authors_ids:
            book.authors.set(authors_ids)

        return redirect("book:index")

    authors = Author.objects.all()
    return render(request, "books/book_create.html", {"authors": authors})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.name = request.POST.get("name")
        book.description = request.POST.get("description")
        book.count = request.POST.get("count")
        book.save()

        authors_ids = request.POST.getlist("authors")
        book.authors.set(authors_ids)

        return redirect("book:book_detail", pk=book.pk)

    authors = Author.objects.all()
    return render(request, "books/book_edit.html", {"book": book, "authors": authors})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book:index")

    return redirect("book:book_detail", pk=pk)

