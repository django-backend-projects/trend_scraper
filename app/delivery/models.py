from django.db import models
from django.utils.translation import gettext_lazy as _

from delivery.utils.models import AbstractBaseModel


class Delivery(AbstractBaseModel):
    account = models.ForeignKey(
        'core.Account',
        on_delete=models.DO_NOTHING,
        verbose_name=_('müştəri'),
        related_name='deliveries'
    )
    order_number = models.CharField(
        _('sifariş nömrəsi'),
        max_length=255,
        db_index=True,
    )
    order_date = models.CharField(
        _('sifariş tarixi'),
        null=True,
        blank=True,
        max_length=255,
    )
    order_receiver = models.CharField(
        _('alıcı'),
        max_length=255,
    )

    def __str__(self):
        return f'{self.account} - {self.order_number}'

    class Meta:
        verbose_name = _('Sifariş')
        verbose_name_plural = _('Sifarişlər')


class Package(AbstractBaseModel):
    account = models.ForeignKey(
        'core.Account',
        on_delete=models.DO_NOTHING,
        verbose_name=_('müştəri'),
        related_name='packages',
        null=True
    )
    delivery = models.ForeignKey(
        'delivery.Delivery',
        on_delete=models.DO_NOTHING,
        verbose_name=_('sifariş'),
        related_name='packages'
    )
    package_number = models.CharField(
        _('bağlama nömrəsi'),
        max_length=255,
        db_index=True,
    )
    cargo_company = models.CharField(
        _('karqo firması'),
        max_length=255,
    )
    tracking_number = models.CharField(
        _('Kargo takip numarası'),
        max_length=255,
    )
    category = models.CharField(
        _('Kateqoriya'),
        max_length=255,
    )
    price = models.CharField(
        _('Qiymət'),
        max_length=255,
    )
    product_count = models.CharField(
        _('Məhsul sayı'),
        max_length=255,
    )
    done = models.BooleanField(
        _('bitib'),
        default=False
    )

    def __str__(self):
        return f'{self.package_number}'

    class Meta:
        verbose_name = _('Bağlama')
        verbose_name_plural = _('Bağlamalar')
