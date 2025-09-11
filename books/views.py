from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm



# Create your views here.

def homepage(request):
    
    books = Book.objects.all()
    print(books)

    return render(request, 'book_list.html', {'books': books})


def add_books(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render a success message
            return redirect('homepage')
    else:
        print("Get the form")
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book:
      book.delete()
    return redirect('homepage')

def update_book(request, id):
    data = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=data)
    if form.is_valid():
        form = form.save(commit=False)
        return redirect('homepage')
    context = {
        'form': form
    }
    return render(request, 'add_book.html', context)
