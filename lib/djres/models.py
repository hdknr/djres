# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from . import methods, querysets


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

    objects = querysets.LangQuerySet.as_manager()

    def __unicode__(self):
        return self.name_local


class LangResource(BaseModel):
    lang = models.ForeignKey(
        Lang, verbose_name=_('Language'),
        null=True, default=None, blank=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL,
        null=True, default=None, blank=True)
    object_id = models.PositiveIntegerField(
        null=True, default=None, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    fieldname = models.CharField(
        _('Field Name'), max_length=20)
    text = models.TextField(
        _('Text Resource'),
        null=True, blank=True, default=None)
    media = models.FileField(
        _('Media Resource'),
        null=True, blank=True, default=None)

    class Meta:
        verbose_name = _('Language Resource')
        verbose_name_plural = _('Language Resource')
