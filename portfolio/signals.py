from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Feedback


@receiver(post_save, sender=Feedback)
def send_feedback_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Новое сообщение',
            f'Новое сообщение #{instance.id}, {instance.name}: {instance.content}.',
            "eugeni.glushcko@yandex.ru",
            ['kamikadze47@gmail.com']
        )
