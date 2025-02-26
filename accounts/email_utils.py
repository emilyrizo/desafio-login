from django.core.mail import send_mail
from django.conf import settings

def send_registration_email(email, name):
    subject = 'Registro no Desafio Técnico da Fidelity'
    message = f'Olá, {name}!\n\nVocê foi registrado com sucesso no desafio técnico da Fidelity!!\n\nAtenciosamente,\nEquipe Fidelity'
    from_email = settings.FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)