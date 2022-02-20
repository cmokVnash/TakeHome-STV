from django.urls import path
from . import views as user_views
from .views import usersList

urlpatterns = [
    path('', user_views.hello, name='hello'),
    path(r'hello',user_views.index, name='hello2'),
    path(r'users', usersList.as_view())
]