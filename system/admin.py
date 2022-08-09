from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from system.models import *
from valley.models import *
from trassir.models import *


### system ###
class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['journal_system', 'journal_act']


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user']


### valley ###
@admin.register(Systems)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ['system_name', 'system_key']


@admin.register(Pumps)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ['pump_name', 'pump_addr']


@admin.register(States)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ['states_system', 'states_dir', 'states_ctrl']


@admin.register(KeyBoard)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ['key_name', 'key_rus', 'key_eng']


### trassir ###
@admin.register(VideoSrv)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ['videosrv_name', 'videosrv_addr']


@admin.register(Cameras)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ['cameras_name']
