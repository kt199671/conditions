from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'condition'
urlpatterns = [
    path('url', views.index, name='index'),
    path('url', views.index, name='index'),
    path('url', views.post, name='post'),
    path('url', views.today, name='today'),
    path('url', views.edit, name='edit'),
    path('url', views.delete, name='delete'),
    path('url', auth_views.LoginView.as_view(template_name="condition/login.html"), name='login'),
    path('url', auth_views.LogoutView.as_view(next_page="condition:index"), name='logout'),
]