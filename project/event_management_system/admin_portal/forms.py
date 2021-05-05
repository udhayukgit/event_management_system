# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.core.validators import validate_email
from .models import Author, Book, Event
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
import datetime

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control",
                "autocomplete" : "off"
            }
        ), validators=[validate_email])
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control",
                "autocomplete" : "off"
            }
        ))


class BookAddForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Title",                
                "class": "form-control"
            }
        ))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description",                
                "class": "form-control"
            }
        ))

    author = forms.ModelChoiceField(
        queryset = Author.objects.all(),
        empty_label = "Select Author",
        widget=forms.Select(
            attrs={
                "placeholder" : "Author",                
                "class": "form-control"
            },
        ))

    class Meta:
        model = Book
        fields = ['title', 'description', 'author']


class EventAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventAddForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk and instance.start_date < datetime.datetime.now().date():
            self.fields['start_date'].widget.attrs['readonly'] = True

        if instance and instance.pk and instance.end_date < datetime.datetime.now().date():
            self.fields['end_date'].widget.attrs['readonly'] = True

    event_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Event Name",                
                "class": "form-control"
            }
        ))

    book = forms.ModelChoiceField(
        queryset = Book.objects.all(),
        empty_label = "Select Book",
        widget=forms.Select(
            attrs={
                "placeholder" : "Book",                
                "class": "form-control"
            },
        ))

    start_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format=('%d/%m/%Y'),
            attrs={
            "placeholder" : "Select date", 
            'class': 'form-control',
        }))

    end_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format=('%d/%m/%Y'),
            attrs={
            "placeholder" : "Select date", 
            'class': 'form-control',
        })
    )

    maximum_participants = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'min': '1',
                "placeholder" : "Maximum Participants",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Event
        fields = ['event_name', 'start_date', 'end_date','maximum_participants','book']