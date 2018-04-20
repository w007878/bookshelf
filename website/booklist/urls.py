from django.urls import path

from . import views

urlpatterns = [
    # Index of booklist
    path('', views.index, name='index'),
    
    # URL for each book
    path('book/<int:book_id>', views.book, name='book')
]
