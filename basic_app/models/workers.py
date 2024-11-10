from basic_app.models.base import *
from django.utils.translation import gettext_lazy as _


class Administrator(BaseModel):
    image = models.ImageField(upload_to='administrators/')
    f_name = models.CharField(max_length=100, verbose_name=_("To'liq ismi"))
    phone = models.CharField(max_length=100, verbose_name=_("Telefon raqami"))
    position = models.CharField(max_length=100, verbose_name=_("Lavozimi"))
    email = models.EmailField(verbose_name=_("Email"), max_length=254, unique=True)
    admission_days = models.CharField(max_length=200, verbose_name=_("Qabul kunlari"))

    class Meta:
        db_table = 'administrators'
        verbose_name = _("Administrator")
        verbose_name_plural = _("Administrators")
