from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Book

def books(request):
    books = Book.objects.all()
    return render_to_response('books/all.html',
                              {'books': books},
                              RequestContext(request)
           )
