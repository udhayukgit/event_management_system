from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, BookAddForm, EventAddForm
from django.contrib import messages
from .models import Author, Book, Event
from django.contrib.auth.decorators import user_passes_test
import datetime

def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

def login_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect("books")
    elif request.user.is_authenticated and not request.user.is_superuser:
        return redirect("dashboard")

    context = {'page_name' : 'admin-login'}
    form = LoginForm(request.POST or None)

    context['msg'] = None
    context['form_errors'] = None
    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            username = get_user(email)
            user = authenticate(username=username, password=password)
            
            if user is not None and username.is_superuser:
                login(request, user)
                return redirect(request.GET.get('next',"books"))
            else:    
                context['msg'] = 'Invalid credentials'    
        else:
            context['msg'] = 'Please fill the required fields'
            context['form_errors'] = form.errors.as_json()
    context['form'] = form

    return render(request, "login.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def books_view(request):
    context = {}
    context['page_name'] = 'books'
    context['book_data'] = Book.objects.all()

    return render(request, "books.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_book_view(request):
    context = {}
    context['page_name'] = 'books'

    form = BookAddForm(request.POST or None)

    context['form_errors'] = None
    if request.method == "POST":

        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been added successfully.')
            return redirect("books")
        else:
            context['form_errors'] = form.errors.as_json()

    context['form'] = form
    return render(request, "add_book.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def edit_book_view(request, pk):
    context = {}
    context['page_name'] = 'books'
    context['page_edit'] = 'edit'
    context['form_errors'] = None
    book = get_object_or_404(Book, pk=pk)
    form = BookAddForm(request.POST or None , instance = book)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been updated successfully.')
            return redirect('books')
        else:
            context['form_errors'] = form.errors.as_json()
    context['form'] = form
    return render(request, "add_book.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)    
    book.delete()
    messages.success(request, 'Book has been deleted successfully.')
    return redirect('books')

@user_passes_test(lambda u: u.is_superuser)
@login_required
def events_view(request,index=False):

    context = {}
    context['page_name'] = 'events'
    context['book_data'] = Event.objects.all()

    return render(request, "events.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_event_view(request):
    context = {}
    context['page_name'] = 'events'

    form = EventAddForm(request.POST or None)

    context['form_errors'] = None
    if request.method == "POST":

        if form.is_valid():
            form.save()
            messages.success(request, 'Event has been added successfully.')
            return redirect("events")
        else:
            context['form_errors'] = form.errors.as_json()

    context['form'] = form
    return render(request, "add_event.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def edit_event_view(request, pk):
    context = {}
    context['page_name'] = 'events'
    context['page_edit'] = 'edit'
    context['form_errors'] = None
    event = get_object_or_404(Event, pk=pk)
    form = EventAddForm(request.POST or None , instance = event)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Event has been updated successfully.')
            return redirect('events')
        else:
            context['form_errors'] = form.errors.as_json()
    context['form'] = form
    return render(request, "add_event.html", context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_event_view(request, pk):
    event = get_object_or_404(Event, pk=pk)    
    event.delete()
    messages.success(request, 'Event has been deleted successfully.')
    return redirect('events')

@user_passes_test(lambda u: u.is_superuser)
@login_required
def participants_view(request, pk, index=False):
    
    context = {}
    context['page_name'] = 'events'
    event = Event.objects.get(id=pk)
    context['event_name'] = event
    context['participant_data'] = event.participant.all()
    
    return render(request, "participants.html", context)

def dahboard_events_view(request):

    context = {}
    context['page_name'] = 'events'
    context['book_data'] = Event.objects.filter(end_date__gte=datetime.date.today())

    return render(request, "dashboard_events.html", context)
