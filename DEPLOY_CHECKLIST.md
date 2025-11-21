# Railway Deployment Checklist

## Before Deploying

- [x] Created Dockerfile for consistent builds
- [x] Created management command to copy media files
- [x] Updated settings.py for production media serving
- [x] Updated urls.py to serve media files
- [x] Created .dockerignore to optimize builds

## Deploy to Railway

1. **Commit all changes:**
```bash
git add .
git commit -m "Fix static files and add Docker support"
git push
```

2. **Railway will automatically:**
   - Detect the Dockerfile
   - Build the Docker image
   - Install all dependencies
   - Collect static files
   - Copy media files to staticfiles
   - Deploy the application

3. **Check deployment logs** in Railway dashboard for any errors

4. **Test your site:**
   - Visit your Railway URL
   - Check if product images are loading
   - Test navigation and functionality

## If Images Still Don't Show

1. Check Railway build logs for errors
2. Verify media files are in Git: `git ls-files media/`
3. SSH into Railway and check: `ls staticfiles/media/products/`
4. Check browser console for 404 errors on image URLs

## Environment Variables (if needed)

Make sure these are set in Railway:
- `PORT` - Automatically set by Railway
- `RAILWAY_ENVIRONMENT` - Automatically set by Railway
- Add any custom variables you need (API keys, etc.)

## Success Indicators

✅ Build completes without errors
✅ "Copied directory: products" appears in build logs
✅ Product images load on the deployed site
✅ Static CSS/JS files load correctly
