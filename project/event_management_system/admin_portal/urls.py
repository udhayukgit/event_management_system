
from django.urls import path
from .views import login_view, books_view, add_book_view, edit_book_view, delete_book_view, dahboard_events_view
from .views import events_view, add_event_view, edit_event_view, delete_event_view, participants_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("books/", books_view, name="books"),
    path("add_book/", add_book_view, name="add_book"),
    path("edit_book/<int:pk>/", edit_book_view, name="edit_book"),
    path("delete_book/<int:pk>/", delete_book_view, name="delete_book"),
    path("events/", events_view, name="events"),
    path("add_event/", add_event_view, name="add_event"),
    path("edit_event/<int:pk>/", edit_event_view, name="edit_event"),
    path("delete_event/<int:pk>/", delete_event_view, name="delete_event"),
    path("participants/<int:pk>/", participants_view, name="participants"),
]
