from abc import ABC,abstractmethod
from dataclasses import dataclass,field
from datetime import datetime,timedelta

def access_token_times(exp:int)->dict:
    a={"iat":datetime.timestamp(datetime.now())}
    b={"exp":datetime.timestamp(datetime.now()+timedelta(minutes=exp))}
    return {**a,**b}

def refresh_token_times(exp:int)->dict:
    a={"iat":datetime.timestamp(datetime.now())}
    b={"exp":datetime.timestamp(datetime.now()+timedelta(minutes=exp))}
    return {**a,**b}

class JwtABC(ABC):
    @abstractmethod
    def get_token(self)->dict:pass

    @abstractmethod
    def decode(self)->dict:pass


@dataclass(init=False)
class JwtOwnAttr:
    jwt_secret:str='utsavsupratim'
    jwt_algos:str='HS512'


@dataclass
class JwtCustomAttr(JwtOwnAttr):
    access_token_exp:int=field(default_factory=int)
    refresh_token_exp:int=field(default_factory=int)

    access_token_exp_iat:dict=field(default_factory=dict,init=False)
    refresh_token_exp_iat:dict=field(default_factory=dict,init=False)

    payload:dict=field(default_factory=dict)
    access_token_dict:dict=field(default_factory=dict,init=False)
    refresh_token_dict:dict=field(default_factory=dict,init=False)

    def __post_init__(self):
        self.access_token_exp_iat=access_token_times(self.access_token_exp)
        self.refresh_token_exp_iat=refresh_token_times(self.refresh_token_exp)

        self.access_token_dict={**self.access_token_exp_iat,**self.payload}
        self.refresh_token_dict={**self.refresh_token_exp_iat,**self.payload}