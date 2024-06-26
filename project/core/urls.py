from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),  
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
]
urlpatterns += staticfiles_urlpatterns()