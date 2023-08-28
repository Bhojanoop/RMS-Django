from micro_auth_service.DTO.resetpassword.resetpassword_dto import ResetPasswordDTO
from micro_auth_service.service.resetpassword.dbService.admindbService import AdminResetPassword
from micro_auth_service.service.resetpassword.dbService.vendordbService import VendorResetPassword

class ResetPasswordService:

    def __init__(self) -> None:
        self._usertypes={
            "ADMIN":AdminResetPassword,
            "VENDOR":VendorResetPassword
        }

    def reset(self,request:object,usertype:str)->dict:
        try:
            dto=ResetPasswordDTO(**request.data)
            return self._usertypes[usertype.upper()]().reset(dto)
        except Exception as e:
            raise Exception(str(e))