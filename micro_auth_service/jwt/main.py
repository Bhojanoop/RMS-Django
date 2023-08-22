import jwt
from micro_auth_service.jwt.config import JwtABC,JwtCustomAttr

class JwtBuilder(JwtABC):

    def __init__(self,payload:dict={},token:str=""):
        self.payload=payload
        self.attr=JwtCustomAttr(payload=self.payload,access_token_exp=13,refresh_token_exp=17)
        self.token=token
    
    
    def get_token(self)->dict:
        try:
            tokens={
                "access_token":jwt.encode(payload=self.attr.access_token_dict,key=self.attr.jwt_secret,algorithm=self.attr.jwt_algos),
                "refresh_token":jwt.encode(payload=self.attr.refresh_token_dict,key=self.attr.jwt_secret,algorithm=self.attr.jwt_algos),
            }
            return tokens
        except Exception as e:
            return str(e)

    def decode(self) -> dict:
        try:
            return jwt.decode(self.token,self.attr.jwt_secret,algorithms=[self.attr.jwt_algos])
        except Exception as e:
            return str(e)

    
