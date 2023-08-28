from micro_auth_service.model.mailverify_model import MailVerify
from datetime import datetime
from micro_auth_service.DTO.mailverify.mailverify_dto import MailVerifyDTO

class DbMailVerifyService:

    def save_record(self,dto:MailVerifyDTO)->bool:
        try:
            if not MailVerify.objects.filter(email=dto.email).exists():
                MailVerify.objects.create(
                    email=dto.email,
                    open_for_verify=True,
                    open_at=str(datetime.timestamp(datetime.now()))
                )
            else:
                mailobj=MailVerify.objects.get(email=dto.email)
                mailobj.open_at=str(datetime.timestamp(datetime.now()))
                mailobj.open_for_verify=True
                mailobj.save()
            return True
        except Exception as e:
            raise Exception(str(e))
