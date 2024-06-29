from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name="Index"),
    path('login',views.login,name="Login"),
    path('signup',views.signup,name="Signup")
]
