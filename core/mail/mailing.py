from decouple import config
from django.core.mail import EmailMessage
from django.template.loader import get_template

class Mail:
    def __init__(self, subject="",body="",mail_receiver=""):
        self.subject=subject
        self.body=body
        self.mail_receiver=mail_receiver
    
    def send(self,data:dict={},template_name:str="",attach_filename:str=""):
        try:
            message = get_template(template_name).render(data)
            email=EmailMessage(self.subject,message,config('EMAIL_HOST_USER'),[self.mail_receiver])
            email.content_subtype = "html"
            if attach_filename:
                email.attach_file(attach_filename)
            email.send()
        except Exception as e:
            raise Exception(str(e))