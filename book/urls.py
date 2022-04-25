from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="index"),
    path('create', views.BookCreateView.as_view(), name='create'),
    path('detail/<int:book_id>/', views.BookDetailView.as_view(), name='detail'),
    path('edit/<int:book_id>/', views.BookUpdateView.as_view(), name='edit'),
    path('delete/<int:book_id>/', views.BookDeleteView.as_view(), name='delete')
    
]