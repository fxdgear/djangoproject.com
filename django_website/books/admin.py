from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_published', 'is_featured', 'authors',)
    search_fields = ('title', 'sub_title', 'description', 'authors')
    list_filter = ('is_featured',)
    
    
admin.site.register(Book, BookAdmin)
