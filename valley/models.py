from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from trassir.models import VideoSrv, Cameras


### Насосы
class Pumps(models.Model):
    class Meta:
        verbose_name = 'Насос'
        verbose_name_plural = 'Насосы'
        ordering = ['pk']

    pump_name = models.CharField(max_length=30, verbose_name='Название')
    pump_addr = models.CharField(max_length=15, verbose_name='Адрес')

    def __str__(self):
        return self.pump_name


### Системы полива
class Systems(models.Model):
    class Meta:
        verbose_name = 'Систему полива'
        verbose_name_plural = 'Системы полива'
        ordering = ['pk']

    system_name = models.CharField(max_length=30, verbose_name='Название')
    system_key = models.CharField(max_length=15, verbose_name='Адрес клавиатуры')
    system_contr = models.CharField(max_length=15, verbose_name='Адрес контроллера')
    system_perc = models.FloatField(verbose_name='Скорость')
    system_depth = models.FloatField(verbose_name='Глубина')
    system_pump = models.ForeignKey(Pumps, on_delete=models.CASCADE, related_name='pump',
                                    verbose_name='Контроллер насоса')
    system_pumpint = models.IntegerField(verbose_name='Вход задвижки насоса')
    system_pumpvalve = models.IntegerField(verbose_name='Реле задвижки насоса')
    system_pumprele1 = models.IntegerField(verbose_name='Реле1 насоса')
    system_pumprele2 = models.IntegerField(default=0, verbose_name='Реле2 насоса')
    system_duet = models.IntegerField(default=0, verbose_name='Связка')
    system_camera = models.OneToOneField(Cameras, on_delete=models.CASCADE, related_name='camera',
                                         verbose_name='Камера', null=True)

    def __str__(self):
        return self.system_name


### Состояния систем полива
class States(models.Model):
    class Meta:
        verbose_name = 'Состояние системы'
        verbose_name_plural = 'Состояния систем'
        ordering = ['pk']

    states_system = models.OneToOneField(Systems, on_delete=models.CASCADE, primary_key=True,
                                         related_name='status', verbose_name='Система')
    states_ctrl = models.BooleanField(default=False, verbose_name='Управление')
    states_fail = models.BooleanField(default=False, verbose_name='Авария')
    DIRECTIONS = [('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')]
    states_dir = models.CharField(max_length=1, choices=DIRECTIONS, default='N', verbose_name='Направление')
    states_wat = models.BooleanField(default=False, verbose_name='Вода')
    states_sis = models.BooleanField(default=False, verbose_name='АвтоСтоп')
    states_valve1 = models.BooleanField(default=False, verbose_name='Задвижка 1')
    states_valve2 = models.BooleanField(default=False, verbose_name='Задвижка 2')
    status_perc = models.FloatField(default=0, verbose_name='Скорость')
    status_depth = models.FloatField(default=0, verbose_name='Глубина')
    status_time = models.DateTimeField(verbose_name='Время запуска', null=True, blank=True)

    def __str__(self):
        return self.states_system.system_name


### Клавиатура
class KeyBoard(models.Model):
    class Meta:
        verbose_name = 'Кнопку'
        verbose_name_plural = 'Клавиатура'
        ordering = ['pk']

    key_name = models.CharField(max_length=15, primary_key=True, default='BtnX-', verbose_name='Id')
    key_eng = models.CharField(max_length=20, verbose_name='Англ')
    key_rus = models.CharField(max_length=20, verbose_name='Рус')
    key_rele1 = models.IntegerField(null=True, verbose_name='Реле 1')
    key_rele2 = models.IntegerField(null=True, verbose_name='Реле 2')
    key_class = models.CharField(max_length=30, null=True, blank=True, verbose_name='Класс')
    key_option1 = models.CharField(max_length=10, null=True, blank=True, verbose_name='Опция 1')
    key_option2 = models.CharField(max_length=10, null=True, blank=True, verbose_name='Опция 2')

    def __str__(self):
        return self.key_name


### Автосоздание статуса при добавлении системы полива
@receiver(post_save, sender=Systems)
def createState(sender, instance, created, **kwargs):
    if created:
        States.objects.create(states_system=instance)
