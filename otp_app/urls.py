from django.urls import path
from . import views

urlpatterns = [
    path('', views.openLoginPage, name="login_page"),
    path('validate_login', views.validateUser, name="validate_login"),
    path('validate_otp', views.validateOTP, name="validate_otp")

]
