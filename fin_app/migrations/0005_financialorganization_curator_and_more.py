# Generated by Django 5.0.6 on 2024-05-09 23:38

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_app', '0004_merge_20240509_2238'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='financialorganization',
            name='curator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='financialorganization',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть введен в формате: '+999999999'. Допускается до 15 цифр.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон'),
        ),
    ]