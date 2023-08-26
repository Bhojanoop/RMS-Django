from django.urls import path
from micro_auth_service.controller.registerController import Register
from micro_auth_service.controller.loginController import Login
from micro_auth_service.controller.getnewTokenController import GetNewToken
from micro_auth_service.controller.otpController import OtpController

urlpatterns = [
    path('register/user-type=<str:usertype>',Register.as_view()),
    path('login/user-type=<str:usertype>',Login.as_view()),
    path('get-new-token/user-type=<str:usertype>&userid=<str:userid>',GetNewToken.as_view()),
    path('otp-verification',OtpController.as_view())
]
