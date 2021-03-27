from django.urls import path
from . import views



urlpatterns = [
    path('url', views.index, name='name'),
    path('url', views.signup, name='name'),
    path('url', views.login_function, name='name'),
]