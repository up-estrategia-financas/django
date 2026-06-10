from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    '''Model representing a book genre (e.g. Science Fiction, Non Fiction).'''
    name = models.CharField(max_length=200, 
                            help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Book(models.Model):
    '''Model representing a boo (bu not specific copy of a book)'''

    title = models.CharField(max_length=200)

    # Foreing Key used because book can only have one author, but authors can have multiples books

    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summmary = models.TextField(max_length=1000, help_text='Enter a brief description of the book.')

    isbn = models.CharField('ISBN', max_length=20, help_text='13 Character [ISBN number]')

    # ManyToManyField used because genre can contain many books.
    # Books can over many genres.
    # Genres class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book.')

    def __str__(self):
        """String for representing the Model object"""
        return self.title

    def get_absolute(self):
        """"Return the url to acess a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])