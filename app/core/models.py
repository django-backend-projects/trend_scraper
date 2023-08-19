from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from delivery.utils.models import AbstractBaseModel


class Account(AbstractBaseModel):
    client_id = models.CharField(
        _('Müştəri ID'),
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        _('Email'),
        unique=True,
    )
    password = models.CharField(
        _('Şifrə'),
        max_length=255,
    )
    is_processing = models.BooleanField(
        _('Proses gedir'),
        default=False
    )
    is_processed = models.BooleanField(
        _('Proses gedib'),
        default=False
    )
    processed_at = models.DateTimeField(
        _("Proses vaxtı"),
        null=True,
        blank=True,
        db_index=True
    )
    slug = models.SlugField(
        _('slug'),
        unique=True,
        max_length=100,
        null=True
    )
    done = models.BooleanField(
        _('Bağlamalar bitib'),
        default=False
    )

    def __str__(self):
        return self.client_id

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.client_id)
        super(Account, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Müştəri")
        verbose_name_plural = _("Müştərilər")


class ExcellAsanInfo(AbstractBaseModel):
    name = models.CharField(
        _('Ad'),
        max_length=255,
    )
    file = models.FileField(
        _('Excell fayl'),
        upload_to='excell_asan_info',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Asan login Excell fayl")
        verbose_name_plural = _("Asan login Excell fayllar")


class ExcellDeclInfo(AbstractBaseModel):
    name = models.CharField(
        _('Ad'),
        max_length=255,
    )
    file = models.FileField(
        _('Excell fayl'),
        upload_to='excell_decl_info',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Deklarasiya Excell fayl")
        verbose_name_plural = _("Deklarasiya Excell fayllar")