from django.urls import path
from micro_auth_service.controller.registerController import Register
from micro_auth_service.controller.loginController import Login
from micro_auth_service.controller.getnewTokenController import GetNewToken
from micro_auth_service.controller.otpController import OtpController
from micro_auth_service.controller.mailVerifyController import MailVerificationController,MailVerify


urlpatterns = [
    path('register/user-type=<str:usertype>',Register.as_view()),
    path('login/user-type=<str:usertype>',Login.as_view()),
    path('get-new-token/user-type=<str:usertype>&userid=<str:userid>',GetNewToken.as_view()),
    path('otp-verification',OtpController.as_view()),
    path('mail-verify',MailVerificationController.as_view()),
    path('bhojanoop/mail-verify/email=<str:email>',MailVerify.as_view())
]
