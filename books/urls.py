from django.urls import path
from .views import homepage
from .views import add_books
from .views import delete_book
from .views import update_book



urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_books/', add_books, name='add_books'),
    path("delete/<int:id>/", delete_book,  name="delete_book"),
    path("update_book/<int:id>/", update_book,  name="update_book"),
   
]