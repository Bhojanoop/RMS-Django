import jwt
from micro_auth_service.jwt.config import JwtABC,JwtCustomAttr

class JwtBuilder(JwtABC):

    def __init__(self,payload:dict={},token:str=""):
        self._payload=payload
        self._token=token
        self._attr=JwtCustomAttr(payload=self._payload,access_token_exp=13,refresh_token_exp=17)
    
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
            return jwt.decode(self._token,self._attr.jwt_secret,algorithms=[self._attr.jwt_algos])
        except Exception as e:
            return str(e)

    
