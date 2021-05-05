from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from admin_portal.models import Event
from django.contrib.auth.decorators import user_passes_test
import datetime

def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

@user_passes_test(lambda u: not u.is_superuser)
def login_view(request):
    if request.user.is_authenticated:
        return redirect("books")

    context = {'page_name' : 'user-signin'}
    form = LoginForm(request.POST or None)

    context['msg'] = None
    context['form_errors'] = None
    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            username = get_user(email)
            user = authenticate(username=username, password=password)
            
            if user is not None and not username.is_superuser:
                login(request, user)
                return redirect(request.GET.get('next',"books"))
            else:    
                context['msg'] = 'Invalid credentials'    
        else:
            context['msg'] = 'Please fill the required fields'
            context['form_errors'] = form.errors.as_json()
    context['form'] = form

    return render(request, "user-login.html", context)

@user_passes_test(lambda u: not u.is_superuser)
def register_view(request):

    context = {'page_name' : 'user-signup'}
    context['msg'] = None
    context['success'] = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = get_user(email)

            if not user:

                form.save()
                
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=user, password=raw_password)
                messages.success(request, 'Account created successfully.')
                return redirect("signin")
            else:
                context['msg'] = 'Email Account already exists.'

        else:
            context['msg'] = 'Please fill the required fields'
            context['form_errors'] = form.errors.as_json()
            print(context['form_errors'])
    else:
        form = SignUpForm()
            
    context['form'] = form

    return render(request, "register.html", context)

@user_passes_test(lambda u: not u.is_superuser)
@login_required
def dashboard_view(request,index=False):
    
    context = {}
    context['page_name'] = 'events'
    context['book_data'] = Event.objects.filter(end_date__gte=datetime.date.today())

    return render(request, "user-events.html", context)


@user_passes_test(lambda u: not u.is_superuser)
@login_required
def participate_view(request, pk):

    event = Event.objects.get(pk=pk)
    event.participant.add(request.user)
    messages.success(request, 'Participated successfully.')

    return redirect("dashboard")

@user_passes_test(lambda u: not u.is_superuser)
@login_required
def exit_participate_view(request, pk):

    event = Event.objects.get(pk=pk,participant__id=request.user.id)
    event.participant.remove(request.user)
    messages.success(request, 'Exited from event successfully.')

    return redirect("dashboard")

