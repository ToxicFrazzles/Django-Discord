from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    pass


class GuildAdmin(admin.ModelAdmin):
    pass


class ChannelAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Guild, GuildAdmin)
admin.site.register(models.Channel, ChannelAdmin)
