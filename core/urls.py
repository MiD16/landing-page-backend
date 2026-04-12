from django.urls import path
from .views import (
    CompanyInfoView,
    ProjectListView,
    ClientListView,
    ContactMessageCreateView
)

urlpatterns = [
    path('company/', CompanyInfoView.as_view(), name='company-info'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-message'),
]
