from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', views.login_view, name='login'),
]