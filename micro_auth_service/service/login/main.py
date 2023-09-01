from micro_auth_service.service.login.loginService.vendorLogin import VendorLogin
from micro_auth_service.service.login.loginService.adminLogin import AdminLogin
from micro_auth_service.DTO.login.login_dto import LoginDTO

class MainLoginService:

    def __init__(self) -> None:
        self._usertypes={
            "ADMIN":AdminLogin,
            "VENDOR":VendorLogin
        }

    def login(self,request,usertype:str)->dict:
        try:
            return self._usertypes[usertype.upper()]().get_tokens(dto=LoginDTO(**request.data),request=request)
        except Exception as e:
            raise Exception(str(e))