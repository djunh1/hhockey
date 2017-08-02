from django.contrib import admin
from hhockeyUser.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'date_joined')
    list_filter = ('date_joined', )

admin.site.register(User, UserAdmin)
