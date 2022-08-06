# Generated by Django 4.1 on 2022-08-06 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('valley', '0002_remove_userprofile_user_delete_journal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(choices=[('C', 'Управление'), ('M', 'Мониторинг')], default='C', max_length=1, verbose_name='Роль')),
                ('user_lang', models.CharField(choices=[('R', 'RUS'), ('E', 'ENG')], default='R', max_length=1, verbose_name='Язык клавиатуры')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователя',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('journal_user', models.CharField(default='admin', max_length=20, verbose_name='Пользователь')),
                ('journal_act', models.CharField(choices=[('R', 'Запуск'), ('S', 'Остановка')], default='S', max_length=1, verbose_name='Действия')),
                ('journal_dir', models.CharField(choices=[('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')], default='N', max_length=1, verbose_name='Направление')),
                ('journal_wat', models.BooleanField(default=False, verbose_name='Вода')),
                ('journal_sis', models.BooleanField(default=False, verbose_name='АвтоСтоп')),
                ('journal_fail', models.BooleanField(default=False, verbose_name='Авария')),
                ('journal_perc', models.FloatField(verbose_name='Скорость')),
                ('journal_depth', models.FloatField(verbose_name='Глубина')),
                ('journal_hours', models.FloatField(verbose_name='Время')),
                ('journal_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='valley.systems', verbose_name='Система')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Журнал',
            },
        ),
    ]
