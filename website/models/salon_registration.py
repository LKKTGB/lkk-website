from django.db import models
from django.utils.translation import ugettext_lazy as _

from website.models.registration import Registration


class SalonRegistration(Registration):
    contestant_name = models.CharField(_('salon_registration_contestant_name'), max_length=100)
    phone_number = models.CharField(_('salon_registration_phone_number'), max_length=20, blank=True)
    email = models.EmailField(_('salon_registration_email'), blank=True)

    class Meta:
        verbose_name = _('salon_registration')
        verbose_name_plural = _('salon_registrations')
