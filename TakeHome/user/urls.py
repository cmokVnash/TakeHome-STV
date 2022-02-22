from django.urls import path
from . import views as user_views
#from .views import usersList

urlpatterns = [
    #path('', user_views.home, name='hello'),
    # path(r'index',user_views.index, name='hello2'),
    # path(r'users', usersList.as_view())
    #login path
    #path('login', user_views.l),
    path('dashboard',user_views.dashBoard),
    path('login', user_views.login),
    path('logout', user_views.logout),
    path('signup',user_views.signup),

    #api paths
    #path('', user_views)

    path('api/login', user_views.loginApi),
    path('api/logout', user_views.logoutApi),
    path('api/signup',user_views.signupApi),
]