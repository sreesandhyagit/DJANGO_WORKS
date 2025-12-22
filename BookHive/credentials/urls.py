from django.urls import path
from credentials import views

urlpatterns = [
    path("register",views.register,name="signup"),
    path("",views.login,name="signin"),
    path("logout",views.logout,name="logout")

]
