# Static Files Fix for Production

## Problem
Product images and media files were not showing on the deployed Railway/Vercel site because these platforms have ephemeral file systems that don't persist uploaded files.

## Solution
Media files are now copied to the staticfiles directory during deployment and served through WhiteNoise.

## Changes Made

### 1. Created Management Command
- `store/management/commands/copy_media_to_static.py` - Copies media files to staticfiles directory

### 2. Updated Settings (`settings.py`)
- Added environment detection for MEDIA_URL
- In production: `MEDIA_URL = '/static/media/'`
- In development: `MEDIA_URL = '/media/'`

### 3. Updated URLs (`urls.py`)
- Media files are now served in all environments (not just DEBUG mode)

### 4. Created Dockerfile
- `Dockerfile` - Railway now uses Docker for consistent builds
- Installs dependencies, collects static files, and copies media files during build

### 5. Updated Configuration Files
- `railway.json` - Set to use Dockerfile builder
- `.dockerignore` - Excludes unnecessary files from Docker build
- `nixpacks.toml` - Alternative configuration (if you switch back to Nixpacks)

## Deployment Steps for Railway

1. Commit and push all changes to your repository:
```bash
git add .
git commit -m "Fix static files for production deployment"
git push
```

2. Railway will automatically redeploy using the Dockerfile
3. The build process will:
   - Install Python dependencies
   - Collect static files
   - Copy media files to staticfiles
   - Run migrations on startup
   - Start Gunicorn server

## Testing Locally

```bash
python manage.py collectstatic --noinput
python manage.py copy_media_to_static
python manage.py runserver
```

## Testing with Docker Locally

```bash
docker build -t ecommerce-app .
docker run -p 8000:8000 -e PORT=8000 ecommerce-app
```

## Important Notes

- All product images in the `media/` folder are committed to Git
- Images are copied to `staticfiles/media/` during deployment
- WhiteNoise serves both static and media files in production
- Railway uses Docker for reliable, consistent builds
- For future uploads, consider using cloud storage (AWS S3, Cloudinary, etc.)

## Troubleshooting

If images still don't show:
1. Check Railway logs for build errors
2. Verify `copy_media_to_static` command ran successfully
3. Check that media files are in your Git repository
4. Verify MEDIA_URL is set correctly in settings.py
