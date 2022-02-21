from django.urls import path
from . import views as user_views
#from .views import usersList

urlpatterns = [
    #path('', user_views.home, name='hello'),
    # path(r'index',user_views.index, name='hello2'),
    # path(r'users', usersList.as_view())
    #login path
    #path('login', user_views.l),
    path('login', user_views.login),
    path('logout', user_views.logout),
    path('signup',user_views.signup),

    #api paths
    #path('', user_views)
]