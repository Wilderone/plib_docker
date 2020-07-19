from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Author, Publishing
from django.shortcuts import render, redirect
from p_library.form import AuthorForm, BookForm, SocialAccountForm, UserForm
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User


import pdb


# Create your views here.


def profilePage(request):
    context = {}
    if request.method == "POST":
        print("POST", request)
    if request.user.is_authenticated:

        context['username'] = request.user.username
        print('REQEST USER', request.user)
        try:
            context['extra'] = SocialAccount.objects.get(
                provider='github', user=request.user).extra_data
        except:

            context['user'] = User.objects.get(username=request.user.username)
            print(context['user'].first_name)

    return render(request, 'profile.html', context)


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == "POST":
        author_formset = AuthorFormSet(
            request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author in author_formset:
                author.save()
            for book in book_formset:
                book.save()
            return HttpResponseRedirect(reverse_lazy('p_library:authors_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
        return render(request, 'manage_books_authors.html', {'author_formset': author_formset, 'book_formset': book_formset})


def author_create_many(request):
    #
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == "POST":
        author_formset = AuthorFormSet(
            request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        # pdb.set_trace()
        return render(request, 'manage_authors.html', {'author_formset': author_formset})


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books')
    template_name = 'manage_books.html'


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    print('INDEX', request.user.username)
    books = Book.objects.all()
    books_list = [i for i in books]
    biblio_data = {'title': 'My library',
                   'books': books_list}

    return HttpResponse(template.render(biblio_data, request))


def show_publishings(request):
    """Показывает издательства и их книги по пути /publish
    Я решил, что вывести просто список издательств будет скучно,
    потому вывел таблицу в которой перечислены издательства, 
    а книги сгруппированы по издательствам(см /publish)."""

    template = loader.get_template('publishings/publishings.html')
    books = Book.objects.all()
    pubs = Publishing.objects.all()
    books_list = [i for i in books]
    pubs_list = [i for i in pubs]
    b_data = {'books': books_list, 'pubs': pubs_list}
    return HttpResponse(template.render(b_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('books')
        else:
            book = Book.objects.filter(id=book_id).first()
            book.copy_count += 1
            book.save()
        return redirect('books')
    else:
        return redirect('books')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('books')
        else:
            book = Book.objects.filter(id=book_id).first()
            if book.copy_count < 1:
                return redirect('books')
            else:
                book.copy_count -= 1
        book.save()
        return redirect('books')
    else:
        return redirect('books')
