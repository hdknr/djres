# -*- coding: utf-8 -*-
# from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from . import models


class LangAdmin(admin.ModelAdmin):
    list_display = ['code', 'name_local', 'name_translated', 'bidi', ]


admin.site.register(models.Lang, LangAdmin)
