from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(_("created date"), default=timezone.now, db_index=True)

    class Meta:
        abstract = True
