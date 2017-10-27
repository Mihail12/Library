from django.shortcuts import render
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from libapp.models import Book, Author
from . import forms
import operator


class IndexController(View):
    def get(self,request):
        num_books=Book.objects.all().count()
        num_authors=Author.objects.count()
        return render(
            request,
            'libapp/index.html',
            context={'num_books':num_books,'num_authors':num_authors},
            )

class BookListView(generic.ListView):
    model = Book
    form_class = forms.BookForm

class BookDetailView(generic.DetailView):
    model = Book
    form_class = forms.BookForm

class AuthorListView(generic.ListView):
    model = Author
    form_class = forms.AuthorForm

class AuthorDetailView(generic.DetailView):
    model = Author
    form_class = forms.AuthorForm

class AuthorCreate(CreateView):
    model = Author
    form_class = forms.AuthorForm
    success_url = reverse_lazy('authors')

class AuthorUpdate(UpdateView):
    model = Author
    form_class = forms.AuthorForm

class AuthorDelete(DeleteView):
    model = Author
    form_class = forms.BookForm
    success_url = reverse_lazy('authors')

class BookCreate(CreateView):
    model = Book
    form_class = forms.BookForm

class BookUpdate(UpdateView):
    model = Book
    form_class = forms.BookForm

class BookDelete(DeleteView):
    model = Book
    form_class = forms.BookForm
    success_url = reverse_lazy('books')


class SearchListView(generic.ListView):
    model = Book
    form_class = forms.BookForm

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains=query)

class NotALinkYet(View):
    def get(self,request):
        return render(request,"libapp/sorry.html")
        

