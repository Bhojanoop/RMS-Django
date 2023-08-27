from micro_auth_service.model.vendor_models import Vendor
import json

class MailVerifyValidationMiddleware:

    def validates(self,request:object):
        try:
            if request.META['REQUEST_METHOD']=='POST':
                body_unicode = request.body.decode('utf-8')
                _data:dict = json.loads(body_unicode)
    
                if Vendor.objects.filter(email=_data['email']).values('email_verified_at')[0]['email_verified_at']:
                    raise Exception("already verified")
            
        except Exception as e:
            raise Exception(str(e))