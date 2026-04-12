from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CompanyInfo, Project, Client, ContactMessage
from .serializers import (
    CompanyInfoSerializer,
    ProjectSerializer,
    ClientSerializer,
    ContactMessageSerializer
)


class CompanyInfoView(generics.RetrieveAPIView):
    """
    GET /api/company/
    Returns company information. Assumes only one CompanyInfo record exists.
    """
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [AllowAny]
    
    def get_object(self):
        # Return the first CompanyInfo object (assuming only one exists)
        return CompanyInfo.objects.first()


class ProjectListView(generics.ListAPIView):
    """
    GET /api/projects/
    Returns list of all projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ClientListView(generics.ListAPIView):
    """
    GET /api/clients/
    Returns list of all clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]


class ContactMessageCreateView(generics.CreateAPIView):
    """
    POST /api/contact/
    Creates a new contact message.
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
