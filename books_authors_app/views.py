from django.shortcuts import redirect, render, HttpResponse
from .models import *

# Create your views here.

######################### Books #########################
def home(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request, "books.html", context)

def addbook(request):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        obj = Book.objects.create(title=title, desc=desc)
        obj.save()
        return redirect("/")

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = book.authors.all()
    no_authors = Author.objects.all().exclude(id__in=authors)
    context = {
        "book":book,
        "authors":authors,
        "no_authors":no_authors
    }
    return render(request, "book.html", context)

def addauthortobook(request, book_id):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        new_author = Author.objects.get(id = request.POST["new_author"])
        book = Book.objects.get(id=book_id)
        book.authors.add(new_author)
        return redirect(f"/book/{book_id}")

######################### Authors #########################
def authors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, "authors.html", context)

def addauthor(request):
    if request.method == "GET":
        return redirect("/authors")
    elif request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        notas = request.POST["notes"]
        obj = Author.objects.create(first_name=first_name, last_name=last_name, notas=notas)
        obj.save()
        return redirect("/authors")

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.books.all()
    no_books = Book.objects.all().exclude(id__in=books)
    context = {
        "author":author,
        "books":books,
        "no_books":no_books
    }
    return render(request, "author.html", context)

def addbooktoauthor(request, author_id):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        new_book = Book.objects.get(id = request.POST["new_book"])
        author = Author.objects.get(id=author_id)
        author.books.add(new_book)
        return redirect(f"/author/{author_id}")