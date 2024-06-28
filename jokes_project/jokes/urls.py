# jokes/urls.py

from django.urls import path
from . import views

app_name = 'jokes'

urlpatterns = [
    path('', views.JokeListView.as_view(), name='list_jokes'),
    path('new/', views.JokeCreateView.as_view(), name='create_joke'),
    path('<int:pk>/', views.JokeDetailView.as_view(), name='joke_detail'),
    path('<int:pk>/edit/', views.JokeUpdateView.as_view(), name='update_joke'),
    path('<int:pk>/delete/', views.JokeDeleteView.as_view(), name='delete_joke'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
