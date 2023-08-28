from core.mail.mailing import Mail
from micro_auth_service.DTO.mailverify.mailverify_dto import MailVerifyDTO
from micro_auth_service.model.vendor_models import Vendor
from datetime import datetime

class MailService:

    def get_username(self,email):
        try:
            return Vendor.objects.filter(email=email).values('full_name')[0]['full_name']
        except Exception as e:
            raise Exception(str(e))

    def sent(self,dto:MailVerifyDTO,request:object)->dict:
        try:
            user_name=self.get_username(dto.email)
            mail=Mail(
                subject="Email Verification from Bhojanoop",
                mail_receiver='utsavchatterjee71@gmail.com'
            )
            sentable_data={
                "user_name":user_name,
                "verification_link":'http://'+request.META['HTTP_HOST']+f'/api/v1/auth/bhojanoop/mail-verify/email={dto.email}&user={user_name}'
            }
            mail.send(
                data=sentable_data,
                template_name='sent_mail_verification.html'
            )
            return {"message":f"verification link send to {dto.email}","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))
        