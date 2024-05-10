from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class FinancialOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название организации")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Номер телефона должен быть введен в формате: '+999999999'. Допускается до 15 цифр.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Телефон") # validators should be a list
    email = models.EmailField(verbose_name="Электронная почта")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    curator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='organizations')

    def __str__(self):
        return self.name
