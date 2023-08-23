from micro_auth_service.service.newtoken.getNewToken.admin import GetNewTokenAdmin
from micro_auth_service.service.newtoken.getNewToken.vendor import GetNewTokenVendor

class NewTokenService:

    def __init__(self) -> None:
        self._usertypes={
            "ADMIN":GetNewTokenAdmin,
            "VENDOR":GetNewTokenVendor
        }
    
    def get(self,usertype:str,userid:str)->dict:
        try:
            return self._usertypes[usertype.upper()]().get_tokens(userid)
        except Exception as e:
            raise Exception(str(e))