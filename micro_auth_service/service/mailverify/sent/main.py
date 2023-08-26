from micro_auth_service.service.mailverify.sent.dbService import DbMailVerifyService
from micro_auth_service.service.mailverify.sent.mailSent import MailService
from micro_auth_service.DTO.mailverify.mailverify_dto import MailVerifyDTO

class MainMailSentService:

    def __init__(self) -> None:
        self._dbservice=DbMailVerifyService
        self._mailservice=MailService

    def send(self,request:object)->dict:
        try:
            dto=MailVerifyDTO(**request.data)
            dbsave=self._dbservice().save_record(dto=dto)
            if dbsave:
                return self._mailservice().sent(dto=dto,request=request)
        except Exception as e:
            raise Exception(str(e))