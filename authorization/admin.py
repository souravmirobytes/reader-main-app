from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    # list_display = ('id', 'email', 'created_at')
    # search_fields = ('id', 'email')
    # # filter_horizontal = ('created_by_facebook', 'created_by_google')
    # list_filter = ('created_by_facebook', 'created_by_google')
    # fieldsets = ()

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
