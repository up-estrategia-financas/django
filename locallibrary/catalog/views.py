from django.shortcuts import render
from django.views import generic
from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': request.session.get('num_visits', 0) + 1,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(LoginRequiredMixin, generic.ListView):
    queryset = Book.objects.order_by('-title') # Get 5 books containing the title war
    context_object_name = 'book_list'
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})