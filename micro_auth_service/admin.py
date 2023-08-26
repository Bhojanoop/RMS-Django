from django.contrib import admin
from micro_auth_service.model.admin_model import Admin
from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.model.customer_model import Customer
from micro_auth_service.model.otp_model import OTP
from micro_auth_service.model.mailverify_model import MailVerify

admin.site.register(Admin)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(OTP)
admin.site.register(MailVerify)