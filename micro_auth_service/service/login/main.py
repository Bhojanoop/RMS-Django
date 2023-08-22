from micro_auth_service.service.login.loginService.vendorLogin import VendorLogin
from micro_auth_service.service.login.loginService.adminLogin import AdminLogin

class MainLoginService:

    def __init__(self) -> None:
        self._logins={
            "ADMIN":AdminLogin,
            "VENDOR":VendorLogin
        }

    def login(self,request,usertype:str)->dict:
        try:
            return self._logins[usertype.upper()]().get_tokens(request)
        except Exception as e:
            raise Exception(str(e))