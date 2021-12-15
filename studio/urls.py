from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='Home'),
    path('post', views.post, name='Post'),
    path('<int:id>/edit', views.edit_post, name='Edit Post')
]