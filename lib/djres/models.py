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
