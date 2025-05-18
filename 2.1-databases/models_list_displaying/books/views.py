from django.core.paginator import Paginator
from django.shortcuts import render
import datetime
from .models import Book


def base(request):
    template ='base.html'
    return render(request, template)

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_view_by_date(request, dt: datetime):
    template = 'books/books_pagi.html'
    books = Book.objects.filter(pub_date=dt)
    paginator = Paginator(books, 3) 
    page_number = request.GET.get('page') 
    page = paginator.get_page(page_number)

    context = {
        'books': page.object_list,
        'page': page  
    }
    return render(request, template, context)
    