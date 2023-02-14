from django.db.models.signals import post_save
from django.dispatch import receiver
from delivery.models import Package


@receiver(post_save, sender=Package)
def update_account(sender, instance, **kwargs):
    account = instance.account
    if all(package.done for package in account.packages.all()):
        account.done = True
        account.save()
