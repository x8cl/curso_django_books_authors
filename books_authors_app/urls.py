from django.urls import path, include
from . import views

app_name = "books_authors_app"
urlpatterns = [
    path("", views.home, name="home"),
    path("addbook", views.addbook, name="addbook"),
    path("book/<book_id>", views.book, name="book"),
    path("book/<book_id>/addauthortobook", views.addauthortobook, name="addauthortobook"),
    path("authors", views.authors, name="authors"),
    path("addauthor", views.addauthor, name="addauthor"),
    path("author/<author_id>", views.author, name="author"),
    path("author/<author_id>/addbooktoauthor", views.addbooktoauthor, name="addbooktoauthor"),
]
