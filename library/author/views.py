from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Author

def index(request):
    authors = Author.get_all()
    return render(request, 'author/index.html', {'authors': authors})

@login_required
def create(request):
    if request.user.role < 1:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')

        Author.create(name, surname, patronymic)
        return redirect('author:index')

    return render(request, 'author/create.html')

@login_required
def delete(request, author_id):
    if request.user.role < 1:
        messages.error(request, "You don't have permissions to delete authors!")
        return redirect('author:index')
    if Author.delete_by_id(author_id):
        messages.success(request, "Author deleted.")
    else:
        messages.error(request, "Could not delete: Author either doesn't exist or is linked to books.")
    return redirect('author:index')
