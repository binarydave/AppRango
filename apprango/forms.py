__author__ = 'gray'

from django import forms
from apprango.models import Category, Page, UserProfile
from django.contrib.auth.models import User


class CatForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter a name for this Category")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ("name", )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter a title for this Page")
    url = forms.URLField(max_length=256, help_text="Enter Page URL")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ("category", )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )