from django.contrib import admin
from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, profilePage
from allauth.account.views import login, logout
from allauth.socialaccount.models import SocialAccount

app_name = 'p_library'
urlpatterns = [
    path('', AuthorList.as_view(), name='author'),
    path('create', AuthorEdit.as_view(), name='author_create'),
    path('create_many', author_create_many, name='author_create_many'),
    path('create_manyes', books_authors_create_many,
         name='book_author_create_many'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/',  profilePage, name='profile'),

]
