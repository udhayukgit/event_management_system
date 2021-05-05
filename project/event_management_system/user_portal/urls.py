
from django.urls import path
from .views import login_view,  register_view, dashboard_view, participate_view, exit_participate_view
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('register/', register_view, name="signup"),
    path("login/", login_view, name="signin"),
    path("logout/", LogoutView.as_view(), name="signout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("participate/<int:pk>/", participate_view, name="participate"),
    path("exit_participate/<int:pk>/", exit_participate_view, name="exit_participate"),
]
