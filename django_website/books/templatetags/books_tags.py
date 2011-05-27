from django import template

from ..models import Book

register = template.Library()

@register.inclusion_tag('books/featured.html')
def render_featured_books(num):
    books = Book.objects.featured()[:num]
    return {
        'books': books,
    }
