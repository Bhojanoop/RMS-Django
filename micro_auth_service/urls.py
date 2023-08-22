from django.urls import path
from micro_auth_service.controller.registerController import Register
from micro_auth_service.controller.loginController import Login

urlpatterns = [
    path('register/user-type=<str:usertype>',Register.as_view()),
    path('login/user-type=<str:usertype>',Login.as_view())
]
