from django.shortcuts import render
from .models import Book, User, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def category(request, foo):
    try:
        category = Category.objects.get(name=foo)
        books = Book.objects.filter(category=category)
        return render(
            request,
            'bookmarket/category.html',{
                'books' : books,
                'category' : category
            }
        )
    except:
        messages.success(
            request,(
                "."
            )
        )
        return redirect('home')

def book(request, pk):
    book = Book.objects.get(id=pk)
    return render(
        request,
        'bookmarket/book.html', {
            'book' : book,
        }
    )


def base(request):
    books = Book.objects.all()
    return render(
        request,
        'bookmarket/main.html',{
            'books' : books,
        }
    )

# def about(request):
#     return render(
#         request,
#         'bookmarket/about.html',
#     )

# def login(request):
#     return render(
#         request, 
#         'bookmarket/login.html',{

#         }
#     )

# def logout(request):
#     pass