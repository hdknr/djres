# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType


class BaseModel(object):
    def get_absolute_url(self):
        return reverse(
            '{0}_{1}_detail'.format(
                self._meta.app_label, self._meta.model_name),
            kwargs={'id': self.id})

    def admin_change_url_name(self):
        return 'admin:{0}_change'.format(self._meta.db_table)

    def admin_change_url(self):
        return reverse(self.admin_change_url_name(), args=(self.id, ))

    @classmethod
    def contenttype(cls):
        return ContentType.objects.get_for_model(cls)

