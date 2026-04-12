# Architecture Company Landing Page Backend

A production-ready Django backend with admin panel to manage content for an architecture company landing page.

## Features

- ✅ Django 5.0.6 with PostgreSQL
- ✅ Django REST Framework API
- ✅ Customized Django Admin Panel
- ✅ Docker & Docker Compose setup
- ✅ CORS configured for React frontend
- ✅ Image upload support
- ✅ Environment-based configuration
- ✅ UUID primary keys
- ✅ Automatic migrations on startup

## Tech Stack

- **Framework**: Django 5.0.6
- **API**: Django REST Framework 3.15.1
- **Database**: PostgreSQL 15
- **Authentication**: Django Admin (built-in)
- **Containerization**: Docker & Docker Compose
- **Media Handling**: Pillow for image processing
- **CORS**: django-cors-headers

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Running with Docker

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd company_landing_page_backend
   ```

2. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Django application
   - Start PostgreSQL database
   - Apply database migrations
   - Create a superuser (username: `admin`, password: `admin`)
   - Start the Gunicorn server on port 8000

3. **Access the application**
   - API: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/
   - API Docs: http://localhost:8000/api/company/ (test endpoints)

### Default Admin Credentials

- **Username**: admin
- **Password**: admin

⚠️ **Important**: Change these credentials in production!

## API Endpoints

### Public Endpoints

#### Get Company Information
```
GET /api/company/
```
Returns company details including name, tagline, description, hero title, and subtitle.

#### Get All Projects
```
GET /api/projects/
```
Returns a paginated list of all architecture projects.

#### Get All Clients
```
GET /api/clients/
```
Returns a paginated list of all clients.

#### Submit Contact Message
```
POST /api/contact/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "I'm interested in your services."
}
```
Creates a new contact message.

### Example API Responses

**Company Info:**
```json
{
  "id": "uuid-here",
  "name": "Architecture Studio",
  "tagline": "Designing Tomorrow's Spaces",
  "description": "We create innovative architectural solutions...",
  "hero_title": "Welcome to Our Studio",
  "hero_subtitle": "Where Vision Meets Precision",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

**Projects List:**
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "uuid-here",
      "title": "Modern Villa",
      "description": "A contemporary residential design...",
      "image": "http://localhost:8000/media/projects/villa.jpg",
      "is_featured": true,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

## Admin Panel Guide

### Accessing Admin Panel

1. Navigate to: http://localhost:8000/admin/
2. Login with admin credentials

### Managing Content

#### Company Information
- Only ONE company info record can exist
- Contains all hero section and company details
- Organized in clear fieldsets

#### Projects
- Add/edit/delete architecture projects
- Upload project images
- Mark projects as featured
- Image preview in list and detail views
- Filter by featured status

#### Clients
- Add/edit/delete clients
- Upload client logos
- Logo preview in list and detail views
- Searchable by name

#### Contact Messages
- View all submitted contact form messages
- Read-only (messages come from the frontend)
- Searchable by name, email, or message content
- Filter by date

### Admin Features

- ✅ Image previews for projects and clients
- ✅ Search functionality on all models
- ✅ Filters for easy navigation
- ✅ Organized fieldsets
- ✅ Read-only metadata fields
- ✅ Responsive interface

## Project Structure

```
company_landing_page_backend/
├── company_landing_page_backend/    # Django project settings
│   ├── settings.py                  # Configuration
│   ├── urls.py                      # Root URL configuration
│   ├── wsgi.py                      # WSGI application
│   └── asgi.py                      # ASGI application
├── core/                            # Main application
│   ├── models.py                    # Database models
│   ├── serializers.py               # DRF serializers
│   ├── views.py                     # API views
│   ├── urls.py                      # App URL routes
│   ├── admin.py                     # Admin configuration
│   └── apps.py                      # App configuration
├── media/                           # User-uploaded files
├── staticfiles/                     # Collected static files
├── Dockerfile                       # Docker configuration
├── docker-compose.yml               # Docker Compose setup
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
└── manage.py                        # Django management script
```

## Environment Variables

Copy `.env.example` to `.env` and configure:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

DB_NAME=arch_db
DB_USER=arch_user
DB_PASSWORD=arch_password
DB_HOST=db
DB_PORT=5432

CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

## Development Commands

### Run Migrations
```bash
docker-compose exec web python manage.py migrate
```

### Create Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

### Collect Static Files
```bash
docker-compose exec web python manage.py collectstatic
```

### Run Django Shell
```bash
docker-compose exec web python manage.py shell
```

### View Logs
```bash
docker-compose logs -f web
docker-compose logs -f db
```

### Stop Containers
```bash
docker-compose down
```

### Stop and Remove Volumes
```bash
docker-compose down -v
```

## Database Models

### CompanyInfo
- `id` (UUID, primary key)
- `name` (CharField)
- `tagline` (CharField)
- `description` (TextField)
- `hero_title` (CharField)
- `hero_subtitle` (CharField)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Project
- `id` (UUID, primary key)
- `title` (CharField)
- `description` (TextField)
- `image` (ImageField)
- `is_featured` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Client
- `id` (UUID, primary key)
- `name` (CharField)
- `logo` (ImageField)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### ContactMessage
- `id` (UUID, primary key)
- `name` (CharField)
- `email` (EmailField)
- `message` (TextField)
- `created_at` (DateTime)

## Security Considerations

- ✅ CSRF protection enabled
- ✅ Passwords hashed (Django default)
- ✅ Admin panel requires authentication
- ✅ Environment variables for sensitive data
- ✅ CORS properly configured
- ✅ SQL injection protection (Django ORM)

## Production Deployment

Before deploying to production:

1. **Change SECRET_KEY**: Generate a strong random key
2. **Set DEBUG=False**: In `.env` file
3. **Update ALLOWED_HOSTS**: Add your domain
4. **Change Admin Password**: Use strong credentials
5. **Use SSL**: Configure HTTPS in production
6. **Backup Database**: Set up regular PostgreSQL backups
7. **Media Storage**: Consider using AWS S3 or similar for production

## Troubleshooting

### Database Connection Issues
```bash
docker-compose down -v
docker-compose up --build
```

### Permission Errors
```bash
sudo chown -R $USER:$USER .
```

### Port Already in Use
Change the port in `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Changed from 8000:8000
```

## License

This project is proprietary and confidential.

## Support

For issues or questions, please contact the development team.
