# Render.com Deployment Instructions

## Fixed Issues
The original deployment failed because:
1. The app was trying to connect to a local 'db' host that doesn't exist on Render
2. The app wasn't binding to the correct port that Render expects

## Files Created/Modified
- `render-entrypoint.sh` - Render-specific startup script
- `render.yaml` - Render service configuration 
- `Dockerfile` - Updated to use render-entrypoint.sh

## Deployment Steps

### 1. Push your code to GitHub
Make sure all files are committed and pushed to your GitHub repository.

### 2. Create Web Service on Render
1. Go to Render.com dashboard
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the repository
5. Configure the service:
   - **Name**: your-app-name (this will be part of the URL)
   - **Region**: Choose nearest region
   - **Branch**: main (or your deployment branch)
   - **Runtime**: Docker
   - **Instance Type**: Free (or paid as needed)

### 3. Set Environment Variables
In the Render dashboard, add these environment variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DB_NAME=your_render_db_name
DB_USER=your_render_db_user  
DB_PASSWORD=your_render_db_password
DB_HOST=your_render_db_host
DB_PORT=5432
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

**Important**: Get the database credentials from Render's PostgreSQL service after you create it.

### 4. Create PostgreSQL Service (if not already created)
1. Click "New +" → "PostgreSQL"
2. Configure the database
3. Copy the connection details to your web service environment variables

### 5. Deploy
Click "Create Web Service" and Render will automatically deploy your application.

## How It Works

### render-entrypoint.sh
- Removes the PostgreSQL wait logic (not needed for managed DB)
- Binds to `$PORT` environment variable (set by Render, usually 10000)
- Runs migrations, collects static files, and starts Gunicorn

### Dockerfile Changes  
- Uses `render-entrypoint.sh` instead of `entrypoint.sh`
- Exposes port 8000 (but actual port is set by Render via $PORT)

### Local Development
To switch back to local development, change the ENTRYPOINT in Dockerfile:
```dockerfile
ENTRYPOINT ["bash", "/app/entrypoint.sh"]
```

## Troubleshooting

If deployment still fails:
1. Check Render logs for specific error messages
2. Verify all environment variables are set correctly
3. Ensure your database service is running and accessible
4. Make sure ALLOWED_HOSTS includes your Render domain

## Expected URL
Your app will be available at: `https://your-app-name.onrender.com`
