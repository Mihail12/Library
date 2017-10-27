from django.contrib import admin

from libapp.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)