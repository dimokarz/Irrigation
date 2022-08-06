from django.db import models
from django.contrib.auth.models import User
from valley.models import Systems


class UserProfile(models.Model):

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователя'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    ROLE = [('C', 'Управление'), ('M', 'Мониторинг')]
    user_role = models.CharField(max_length=1, choices=ROLE, default='C', verbose_name='Роль')
    LANGUAGE = [('R', 'RUS'), ('E', 'ENG')]
    user_lang = models.CharField(max_length=1, choices=LANGUAGE, default='R', verbose_name='Язык клавиатуры')


class Journal(models.Model):

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Журнал'

    journal_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    journal_system = models.ForeignKey(Systems, on_delete=models.CASCADE, verbose_name='Система', null=True)
    journal_user = models.CharField(max_length=20, default='admin', verbose_name='Пользователь')
    ACTIONS = [('R', 'Запуск'), ('S', 'Остановка')]
    journal_act = models.CharField(max_length=1, choices=ACTIONS, default='S', verbose_name='Действия')
    DIRECTIONS = [('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')]
    journal_dir = models.CharField(max_length=1, choices=DIRECTIONS, default='N', verbose_name='Направление')
    journal_wat = models.BooleanField(default=False, verbose_name='Вода')
    journal_sis = models.BooleanField(default=False, verbose_name='АвтоСтоп')
    journal_fail = models.BooleanField(default=False, verbose_name='Авария')
    journal_perc = models.FloatField(verbose_name='Скорость')
    journal_depth = models.FloatField(verbose_name='Глубина')
    journal_hours = models.FloatField(verbose_name='Время')

    def __str__(self):
        return self.journal_system.system_name
