# Railway Deployment Guide

## Prerequisites
- GitHub account
- Railway account (sign up at https://railway.app)
- Your code pushed to GitHub

## Step-by-Step Deployment

### 1. Prepare Your Repository
```bash
# Make sure all changes are committed
git add .
git commit -m "Prepare for Railway deployment"
git push origin master
```

### 2. Create Railway Project

1. Go to https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Authorize Railway to access your GitHub
5. Select your `E-commerce-website-` repository

### 3. Add PostgreSQL Database

1. In your Railway project dashboard, click "New"
2. Select "Database" → "Add PostgreSQL"
3. Railway will automatically create a PostgreSQL database
4. The `DATABASE_URL` environment variable will be set automatically

### 4. Configure Environment Variables

In Railway project settings, add these variables:

```
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DEBUG=False
```

**Important:** Generate a secure SECRET_KEY. You can use this Python command:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Deploy

Railway will automatically:
- Detect your Python project
- Install dependencies from `requirements.txt`
- Run migrations
- Collect static files
- Copy media files to static
- Start the Gunicorn server

### 6. Create Admin User

After deployment, you need to create an admin user:

1. Go to your Railway project
2. Click on your service
3. Go to "Settings" tab
4. Scroll to "Service" section
5. Click "Open Terminal" or use Railway CLI

Run this command in the terminal:
```bash
python manage.py create_admin
```

This will create:
- Username: `admin`
- Password: `admin123`

**Change this password immediately after first login!**

### 7. Access Your Site

1. In Railway dashboard, find your service
2. Click on "Settings" tab
3. Under "Networking", you'll see your public URL
4. Click "Generate Domain" if not already generated
5. Your site will be available at: `https://your-app-name.up.railway.app`

### 8. Access Admin Panel

Visit: `https://your-app-name.up.railway.app/admin/`
- Username: `admin`
- Password: `admin123`

## Troubleshooting

### Build Fails
- Check Railway logs for errors
- Ensure all dependencies are in `requirements.txt`
- Verify Python version in `runtime.txt`

### Static Files Not Loading
- Check if `collectstatic` ran successfully in logs
- Verify `STATIC_ROOT` and `STATIC_URL` in settings
- Check WhiteNoise is installed and configured

### Database Errors
- Ensure PostgreSQL database is added to project
- Check `DATABASE_URL` environment variable is set
- Verify migrations ran successfully

### Media Files Not Showing
- Check if `copy_media_to_static` command ran
- Verify media files are in your Git repository
- Check logs for "Copied directory: products"

## Updating Your Deployment

When you make changes:
```bash
git add .
git commit -m "Your changes"
git push origin master
```

Railway will automatically redeploy your application.

## Important Notes

1. **Database**: Railway uses PostgreSQL in production, SQLite locally
2. **Media Files**: Uploaded files are stored in static directory (not persistent)
3. **For Production**: Consider using AWS S3 or Cloudinary for media files
4. **Security**: Change admin password and SECRET_KEY immediately
5. **Environment Variables**: Never commit `.env` file to Git

## Railway CLI (Optional)

Install Railway CLI for easier management:
```bash
npm install -g @railway/cli
railway login
railway link
railway logs
```

## Cost

Railway offers:
- Free tier: $5 credit per month
- Hobby plan: $5/month
- Pro plan: $20/month

Your e-commerce site should run fine on the free tier for development/testing.

## Support

- Railway Docs: https://docs.railway.app
- Django Docs: https://docs.djangoproject.com
- Project Issues: Check your GitHub repository issues
