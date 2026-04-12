from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import ngettext
from django.contrib import messages


class CustomUserAdmin(UserAdmin):
    """Custom User admin with simplified interface and no groups."""
    
    # Remove groups from the admin
    filter_horizontal = ()
    
    # Simplified fieldsets without groups and important dates
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')
        }),
    )
    
    # Fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    
    def has_delete_permission(self, request, obj=None):
        """Completely forbid user deletion."""
        return False
    
    def has_module_permission(self, request):
        """Ensure user module is visible."""
        return True
    
    def delete_model(self, request, obj):
        """Override single object deletion - forbid it."""
        self.message_user(
            request,
            "User deletion is not allowed.",
            messages.ERROR
        )
        return
    
    def delete_queryset(self, request, queryset):
        """Override bulk deletion - forbid it."""
        self.message_user(
            request,
            "User deletion is not allowed.",
            messages.ERROR
        )


# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Unregister Groups to hide it completely from admin
if admin.site.is_registered(Group):
    admin.site.unregister(Group)
