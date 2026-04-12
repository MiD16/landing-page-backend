from django.core.management.base import BaseCommand
from core.models import CompanyInfo, Project, Client


class Command(BaseCommand):
    help = 'Creates initial demo data for the architecture company landing page'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating initial demo data...'))

        # Create Company Info (only if it doesn't exist)
        if not CompanyInfo.objects.exists():
            CompanyInfo.objects.create(
                name='Architecture Studio',
                tagline='Designing Tomorrow\'s Spaces Today',
                description='We are a leading architecture firm specializing in innovative, sustainable, and beautiful designs. Our team of experienced architects brings your vision to life with precision and creativity.',
                hero_title='Welcome to Architecture Studio',
                hero_subtitle='Where Vision Meets Precision in Every Design',
                # Who We Are Section
                years_experience=15,
                projects_completed=150,
                total_built_area='500,000+ m²',
                # Contact Section
                contact_email='hello@archstudio.com',
                contact_phone='+1 (555) 123-4567',
                contact_address='123 Architecture Ave, Design City, DC 12345',
                # Footer Social Media
                instagram_url='https://instagram.com/archstudio',
                facebook_url='https://facebook.com/archstudio',
                linkedin_url='https://linkedin.com/company/archstudio',
            )
            self.stdout.write(self.style.SUCCESS('✓ Company info created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Company info already exists'))

        # Create sample projects
        if Project.objects.count() == 0:
            self.stdout.write(self.style.WARNING('⚠ No projects created (requires image uploads via admin)'))
        else:
            self.stdout.write(self.style.SUCCESS(f'✓ {Project.objects.count()} projects exist'))

        # Create sample clients
        if Client.objects.count() == 0:
            self.stdout.write(self.style.WARNING('⚠ No clients created (requires logo uploads via admin)'))
        else:
            self.stdout.write(self.style.SUCCESS(f'✓ {Client.objects.count()} clients exist'))

        self.stdout.write(self.style.SUCCESS('\nInitial data setup complete!'))
        self.stdout.write(self.style.WARNING('\nNext steps:'))
        self.stdout.write('1. Access admin panel at: http://localhost:8000/admin/')
        self.stdout.write('2. Login with admin credentials')
        self.stdout.write('3. Add projects and clients with images')
        self.stdout.write('4. Test API endpoints at: http://localhost:8000/api/')
