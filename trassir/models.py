from django.db import models


class VideoSrv(models.Model):

    class Meta:
        verbose_name = 'Видео сервер'
        verbose_name_plural = 'Видео серверы'
        ordering = ['pk']

    videosrv_name = models.CharField(max_length=30, verbose_name='Название')
    videosrv_addr = models.CharField(max_length=15, verbose_name='Адрес')
    videosrv_https = models.IntegerField(null=True, verbose_name='Порт HTTPS')
    videosrv_http = models.IntegerField(null=True, verbose_name='Порт HTTP')
    videosrv_user = models.CharField(max_length=15, verbose_name='Пользователь')
    videosrv_password = models.CharField(max_length=30, verbose_name='Пароль')

    def __str__(self):
        return self.videosrv_name


class Cameras(models.Model):

    class Meta:
        verbose_name = 'Камеру'
        verbose_name_plural = 'Камеры'
        ordering = ['pk']

    cameras_srv = models.ForeignKey(VideoSrv, on_delete=models.CASCADE, related_name='cameras_srv',
                                    verbose_name='Видеосервер')
    cameras_name = models.CharField(max_length=30, verbose_name='Название')
    cameras_channel = models.CharField(max_length=8, verbose_name='Id канала')

    def __str__(self):
        return self.cameras_name