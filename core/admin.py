from django.contrib import admin
from django.utils.html import format_html
from .models import CompanyInfo, Project, Client, ContactMessage

# Import custom user admin to prevent self-deletion
from . import user_admin


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    """Admin interface for CompanyInfo model."""
    
    list_display = ['name', 'tagline', 'created_at', 'updated_at']
    search_fields = ['name', 'tagline', 'description']
    readonly_fields = ['id', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'description')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Metadata', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Allow only one CompanyInfo record
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for Project model with image preview."""
    
    list_display = ['title', 'is_featured', 'image_preview', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']
    readonly_fields = ['id', 'image_preview_large', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Project Details', {
            'fields': ('title', 'description', 'is_featured')
        }),
        ('Image', {
            'fields': ('image', 'image_preview_large')
        }),
        ('Metadata', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        """Small image preview for list display."""
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = "Preview"
    
    def image_preview_large(self, obj):
        """Large image preview for detail view."""
        if obj.image:
            return format_html(
                '<img src="{}" width="300" style="max-width: 100%;" />',
                obj.image.url
            )
        return "No Image"
    image_preview_large.short_description = "Image Preview"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Admin interface for Client model with logo preview."""
    
    list_display = ['name', 'logo_preview', 'created_at']
    search_fields = ['name']
    readonly_fields = ['id', 'logo_preview_large', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'logo')
        }),
        ('Logo Preview', {
            'fields': ('logo_preview_large',)
        }),
        ('Metadata', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def logo_preview(self, obj):
        """Small logo preview for list display."""
        if obj.logo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: contain;" />',
                obj.logo.url
            )
        return "No Logo"
    logo_preview.short_description = "Logo"
    
    def logo_preview_large(self, obj):
        """Large logo preview for detail view."""
        if obj.logo:
            return format_html(
                '<img src="{}" width="300" style="max-width: 100%;" />',
                obj.logo.url
            )
        return "No Logo"
    logo_preview_large.short_description = "Logo Preview"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin interface for ContactMessage model."""
    
    list_display = ['name', 'email', 'created_at', 'message_preview']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['id', 'name', 'email', 'message', 'created_at']
    
    list_display_links = ['name']
    
    def message_preview(self, obj):
        """Show first 50 characters of message."""
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_preview.short_description = "Message Preview"
    
    def has_add_permission(self, request):
        # Contact messages should only be created via the API/form
        return False
    
    def has_change_permission(self, request, obj=None):
        # Contact messages should be read-only
        return False
