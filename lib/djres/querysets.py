from django.db.models import QuerySet
from django.conf import settings
from django.utils import translation


class LangQuerySet(QuerySet):

    def get_lang(self, name):
        info = translation.get_language_info(name)
        lang, created = self.get_or_create(code=info['code'])
        if created:
            map(lambda (k, v): setattr(lang, k, v), info.items())
            lang.save()
        return lang

    def supported_langs(self):
        langs = getattr(settings, 'SUPPORTED_LANGS', [])
        return [self.get_lang(name) for name in langs]
