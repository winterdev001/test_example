from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book_app/index.html"
    context_object_name = 'book_lists'
    
class BookCreateView(SuccessMessageMixin,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_app/create.html'
    success_url = reverse_lazy('index')
    success_message = "Book was created successfully"
    
class BookDetailView(SuccessMessageMixin,DetailView):
    model = Book
    template_name = "book_app/detail.html"
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'

class BookUpdateView(SuccessMessageMixin,UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_app/edit.html"
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'
    success_message = "Book was updated successfully"
    def get_success_url(self):
        return reverse('detail', kwargs={'book_id':self.object.pk})
    
class BookDeleteView(SuccessMessageMixin,DeleteView):
    model = Book
    template_name = 'book_app/delete.html'
    success_url = reverse_lazy('index')
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'
    success_message = "Book was Deleted successfully"
    
