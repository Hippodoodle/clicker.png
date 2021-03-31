from django.contrib import admin
from clicker_app.models import Achievement,  Upgrade, Account, OwnsUpgrade


class AchievementAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ('name', 'description')


class UpgradeAdmin(admin.ModelAdmin):
    fields = ['name', 'cost', 'effect', 'auto_click']
    list_display = ('name', 'cost', 'effect', 'auto_click')


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Upgrade, UpgradeAdmin)
admin.site.register(Account)
admin.site.register(OwnsUpgrade)
