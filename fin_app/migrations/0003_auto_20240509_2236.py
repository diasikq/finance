from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_user_groups(apps, schema_editor):
    # Получение модели в контексте миграции
    FinancialOrganization = apps.get_model('fin_app', 'FinancialOrganization')
    ct = ContentType.objects.get_for_model(FinancialOrganization)

    # Создание группы для кураторов
    curator_group, _ = Group.objects.get_or_create(name='Куратор')
    curator_perms = ['add_financialorganization', 'change_financialorganization']
    for codename in curator_perms:
        perm = Permission.objects.get(codename=codename, content_type=ct)
        curator_group.permissions.add(perm)

    # Создание группы для ревьюеров
    reviewer_group, _ = Group.objects.get_or_create(name='Ревьюер')
    reviewer_perms = ['view_financialorganization', 'change_financialorganization']
    for codename in reviewer_perms:
        perm = Permission.objects.get(codename=codename, content_type=ct)
        reviewer_group.permissions.add(perm)

class Migration(migrations.Migration):

    dependencies = [
        # Указать зависимости от других миграций, например:
        ('fin_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_user_groups),
    ]
