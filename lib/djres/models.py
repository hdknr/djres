# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import methods


class BaseModel(models.Model, methods.BaseModel):
    created_at = models.DateTimeField(
        _(u'Created Datetime'), auto_now_add=True)
    updated_at = models.DateTimeField(
        _(u'Updated Datetime'), auto_now=True)

    class Meta:
        abstract = True


class Lang(BaseModel):
    code = models.CharField(
        _('Language Code'), max_length=10, unique=True, db_index=True)
    name_local = models.CharField(
        _('Language Name'), max_length=20, null=True, blank=True, default=None)
    name_translated = models.CharField(
        _('Language Name Translated'),
        max_length=20, null=True, blank=True, default=None)
    bidi = models.BooleanField(
        _('Bi Direction'), default=False)

    class Meta:
        verbose_name = _('Supported Language')
        verbose_name_plural = _('Supported Language')
