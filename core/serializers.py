from rest_framework import serializers
from .models import CompanyInfo, Project, Client, ContactMessage


class CompanyInfoSerializer(serializers.ModelSerializer):
    """Serializer for CompanyInfo model."""
    
    class Meta:
        model = CompanyInfo
        fields = [
            'id', 'name', 'tagline', 'description',
            'hero_title', 'hero_subtitle', 'hero_image',
            'who_we_are_image', 'years_experience', 'projects_completed', 'total_built_area',
            'contact_email', 'contact_phone', 'contact_address',
            'instagram_url', 'facebook_url', 'linkedin_url',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'is_featured', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client model."""
    
    class Meta:
        model = Client
        fields = ['id', 'name', 'logo', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ContactMessageSerializer(serializers.ModelSerializer):
    """Serializer for ContactMessage model (used for submitting contact forms)."""
    
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
