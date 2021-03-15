from django.contrib import admin
from clicker_app.models import Achievement,  Upgrade, Account, OwnsUpgrade

admin.site.register(Achievement)
admin.site.register(Upgrade)
admin.site.register(Account)
admin.site.register(OwnsUpgrade)
