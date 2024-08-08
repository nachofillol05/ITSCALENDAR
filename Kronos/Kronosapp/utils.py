from django.contrib.auth import get_user_model
from django.urls import reverse
from email.message import EmailMessage
import smtplib
from .serializers.user_serializer import RegisterSerializer

from .models import CustomUser
from django.http import HttpResponse



user = get_user_model()

def send_email(receiver, subject, message, sender="proyecto.villada.solidario@gmail.com"):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(sender, "bptf tqtv hjsb zfpl")
    smtp.sendmail(sender, receiver, email.as_string())
    smtp.quit()

def register_user(request, data):
    serializer = RegisterSerializer(data=data)
    if not serializer.is_valid():
        return False, serializer.errors
    user = serializer.save()
    verification_url = request.build_absolute_uri(
        reverse('verify-email', args=[str(user.verification_token)])
    )
    SUBJECT = "Verifica tu correo electrónico"
    MESSAGE = 'Haz clic en el enlace para verificar tu correo electrónico: ' + verification_url
    send_email(receiver=user.email, subject=SUBJECT, message=MESSAGE)
    return True, serializer.data


def verify_email(request,token):
    try:
        user = CustomUser.objects.get(verification_token=token)
        if user.email_verified:
            return HttpResponse('Correo electrónico ya verificado', status=400)
        else:
            user.email_verified = True
            user.save()
            return HttpResponse('Correo electrónico verificado con éxito', status=200)
    except CustomUser.DoesNotExist:
        return HttpResponse('Token de verificación no válido', status=404)
    