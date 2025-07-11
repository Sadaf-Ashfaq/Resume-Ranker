from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('ranker/', views.resume_ranker_view, name='ranker'),
    path('internship/', views.internship_program_view, name='internship_program'),
    path('about/', views.about_view, name='about'),
    path('logout/', views.logout_view, name='logout'),
]

