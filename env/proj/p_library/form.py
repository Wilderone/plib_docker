from django import forms
from p_library.models import Author, Book
from django.forms import formset_factory
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.forms import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SocialAccountForm(forms.ModelForm):

    class Meta:
        model = SocialAccount
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


AuthorFormSet = formset_factory(AuthorForm)
BookFormSet = formset_factory(BookForm)
