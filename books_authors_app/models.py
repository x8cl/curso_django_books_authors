from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "books_authors_app"
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notas = models.TextField(null=True, blank=True)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "books_authors_app"

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def __repr__(self):
        return self.first_name + " " + self.last_name
