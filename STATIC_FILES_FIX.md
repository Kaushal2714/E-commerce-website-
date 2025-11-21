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

### 4. Updated Build Scripts
- `build_files.sh` - Added `copy_media_to_static` command
- `railway.json` - Added `copy_media_to_static` to startCommand

## Deployment Steps

1. Commit and push all changes to your repository
2. Railway/Vercel will automatically redeploy
3. The build process will:
   - Run migrations
   - Collect static files
   - Copy media files to staticfiles
   - Start the server

## Testing Locally

```bash
python manage.py collectstatic --noinput
python manage.py copy_media_to_static
python manage.py runserver
```

## Important Notes

- All product images in the `media/` folder are committed to Git
- Images are copied to `staticfiles/media/` during deployment
- WhiteNoise serves both static and media files in production
- For future uploads, consider using cloud storage (AWS S3, Cloudinary, etc.)
