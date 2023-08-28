import jwt
from micro_auth_service.jwt.config import JwtABC,JwtCustomAttr
from decouple import config

class JwtBuilder(JwtABC):

    def __init__(self,payload:dict={},token:str=None,request:object=None):
        self._payload=payload
        self._token=token
        if request:
            if request.user_agent.is_mobile:
                access_token_exp=2880
                refresh_token_exp=20160
            else:
                access_token_exp=40
                refresh_token_exp=45
        if payload:
            self._attr=JwtCustomAttr(payload=self._payload,access_token_exp=access_token_exp,refresh_token_exp=refresh_token_exp)
    
    def get_token(self)->dict:
        try:
            tokens={
                "access_token":jwt.encode(payload=self._attr.access_token_dict,key=self._attr.jwt_secret,algorithm=self._attr.jwt_algos),
                "refresh_token":jwt.encode(payload=self._attr.refresh_token_dict,key=self._attr.jwt_secret,algorithm=self._attr.jwt_algos),
            }
            return tokens
        except Exception as e:
            return str(e)

    def decode(self) -> dict:
        try:
            return jwt.decode(self._token,config('JWT_SECRET'),algorithms=config('JWT_ALGO'))
        except Exception as e:
            return str(e)

    
