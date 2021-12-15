from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='Home'),
    path('post', views.post, name='Post'),
    path('login', views.login, name='Login'),
    path('signup', views.signup, name='Signup'),
    path('logout', views.logout, name='Logout'),
    path('comment', views.comment, name='Comment'),
    path('account', views.account, name='Account'),
    path('<str:username>', views.user, name='User'),
    path('<int:id>/edit', views.edit_post, name='Edit Post'),
    path('<str:username>/update', views.update_profile, name='Update')
]