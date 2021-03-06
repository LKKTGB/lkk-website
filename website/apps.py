from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WebsiteConfig(AppConfig):
    name = 'website'
    verbose_name = _('app_website')

    def ready(self):
        from website import signals
