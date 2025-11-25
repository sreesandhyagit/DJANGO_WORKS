from django.urls import path
from credentials import views

urlpatterns = [
    path("",views.register,name="signup")
]
