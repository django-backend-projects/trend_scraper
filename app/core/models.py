from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
# django.setup()

from delivery.utils.models import AbstractBaseModel


class Account(AbstractBaseModel):
    client_id = models.CharField(_("Müştəri ID"), max_length=255, unique=True)
    email = models.EmailField(
        _("Email"),
        unique=True,
    )
    password = models.CharField(
        _("Şifrə"),
        max_length=255,
    )
    is_processing = models.BooleanField(_("Proses gedir"), default=False)
    is_processed = models.BooleanField(_("Proses gedib"), default=False)
    processed_at = models.DateTimeField(
        _("Proses vaxtı"), null=True, blank=True, db_index=True
    )
    slug = models.SlugField(_("slug"), unique=True, max_length=100, null=True)
    done = models.BooleanField(_("Bağlamalar bitib"), default=False)

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
        _("Ad"),
        max_length=255,
    )
    file = models.FileField(
        _("Excell fayl"), upload_to="excell_asan_info", null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Asan login Excell fayl")
        verbose_name_plural = _("Asan login Excell fayllar")


class ExcellDeclInfo(AbstractBaseModel):
    name = models.CharField(
        _("Ad"),
        max_length=255,
    )
    file = models.FileField(
        _("Excell fayl"), upload_to="excell_decl_info", null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Deklarasiya Excell fayl")
        verbose_name_plural = _("Deklarasiya Excell fayllar")


class FailedDeclar(AbstractBaseModel):
    fin_code = models.CharField(
        _("Fin kod"),
        max_length=255,
    )
    password = models.CharField(
        _("Şifrə"),
        max_length=255,
    )
    dec_id = models.CharField(
        _("Göndəriş ID"),
        max_length=255,
    )
    reason = models.CharField(
        _("Səbəb"),
        max_length=255,
    )
    is_active = models.BooleanField(_("Aktiv"), default=True)

    def __str__(self):
        return self.dec_id

    class Meta:
        verbose_name = _("Uğursuz deklarasiya")
        verbose_name_plural = _("Uğursuz deklarasiyalar")


class Declaration(AbstractBaseModel):
    fin_code = models.CharField(
        _("Fin kod"),
        max_length=255,
    )
    password = models.CharField(
        _("Şifrə"),
        max_length=255,
    )
    user_id = models.CharField(
        _("İstifadəçi ID"),
        max_length=255,
    )
    dec_id = models.CharField(
        _("Declaration ID"),
        max_length=255,
    )
    is_declared = models.BooleanField(_("Bəyan olunub"), default=False)

    def __str__(self):
        return f"{self.user_id} - {self.dec_id}"


class Interval(AbstractBaseModel):
    price = models.DecimalField(_("Qiymət"), max_digits=10, decimal_places=2)
    start_interval = models.IntegerField(_("Start Interval"), default=0)
    end_interval = models.IntegerField(_("End Interval"), default=0)
    is_active = models.BooleanField(_("Aktiv"), default=True)

    def __str__(self):
        return f"{self.start_interval} - {self.end_interval}"
    
    class Meta:
        verbose_name = _("Interval")
        verbose_name_plural = _("Intervals")