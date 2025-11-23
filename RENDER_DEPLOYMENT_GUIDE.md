# Render Deployment Guide - Django Ecommerce Project

## Step-by-Step Deployment Instructions

### Prerequisites
1. GitHub account with your code pushed
2. Render account (sign up at https://render.com)
3. MySQL database (PlanetScale, Railway, or AWS RDS)

---

## Part 1: Set Up MySQL Database

### Option A: PlanetScale (Recommended - Free Tier)
1. Go to https://planetscale.com and sign up
2. Create a new database named `ecommerce_data`
3. Click "Connect" and get your connection details:
   - Host
   - Username
   - Password
   - Database name
4. Keep these credentials handy

### Option B: Railway MySQL
1. Go to https://railway.app
2. Create new project → Add MySQL
3. Get connection details from the MySQL service
4. Note down: Host, Port, Username, Password, Database

---

## Part 2: Deploy to Render

### Step 1: Create Web Service
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub account
4. Select repository: `Kaushal2714/E-commerce-website-`
5. Click "Connect"

### Step 2: Configure Build Settings
Fill in these details:

**Name:** `ecommerce-app` (or your preferred name)

**Region:** Choose closest to you

**Branch:** `master`

**Root Directory:** `ecommerce_project`

**Runtime:** `Python 3`

**Build Command:**
```bash
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

**Start Command:**
```bash
gunicorn ecommerce_project.wsgi:application
```

**Instance Type:** Free (or paid for better performance)

### Step 3: Add Environment Variables
Click "Advanced" → "Add Environment Variable" and add these:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.12.0` | Python version |
| `DEBUG` | `False` | Production mode |
| `SECRET_KEY` | Generate new key* | Django secret key |
| `DB_NAME` | Your MySQL database name | From Part 1 |
| `DB_USER` | Your MySQL username | From Part 1 |
| `DB_PASSWORD` | Your MySQL password | From Part 1 |
| `DB_HOST` | Your MySQL host URL | From Part 1 |
| `DB_PORT` | `3306` | MySQL port |
| `RAZORPAY_KEY_ID` | Your Razorpay key | Payment gateway |
| `RAZORPAY_KEY_SECRET` | Your Razorpay secret | Payment gateway |

*To generate SECRET_KEY, run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Step 4: Deploy
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Render will automatically:
   - Install dependencies
   - Collect static files
   - Run migrations
   - Start your app

---

## Part 3: Post-Deployment

### Step 1: Create Superuser
1. Go to your Render dashboard
2. Click on your service
3. Go to "Shell" tab
4. Run:
```bash
python manage.py createsuperuser
```
5. Follow prompts to create admin account

### Step 2: Test Your Site
1. Visit your Render URL: `https://your-app-name.onrender.com`
2. Test:
   - Homepage loads ✓
   - Product images display ✓
   - User registration works ✓
   - Login works ✓
   - Add to cart works ✓
   - Admin panel: `https://your-app-name.onrender.com/admin`

### Step 3: Upload Product Images
Since media files aren't in Git:
1. Login to admin panel
2. Go to Products
3. Re-upload product images
4. Or use Django shell to bulk update

---

## Troubleshooting

### Issue: Bad Request (400)
**Solution:** The code is already fixed to auto-detect Render hostname. Just redeploy.

### Issue: Database Connection Error
**Solution:** 
- Verify all DB_* environment variables are correct
- Check MySQL database is running
- Ensure database allows connections from Render IPs

### Issue: Static Files Not Loading
**Solution:**
- Run: `python manage.py collectstatic --no-input`
- Check STATIC_ROOT and STATIC_URL in settings
- WhiteNoise is already configured

### Issue: Images Not Showing
**Solution:**
- For production, consider using cloud storage (AWS S3, Cloudinary)
- Or re-upload images through admin panel
- Media files need persistent storage on Render

---

## Important Notes

### Media Files Storage
Render's free tier has ephemeral storage. For persistent media files:

**Option 1: Cloudinary (Recommended)**
1. Sign up at https://cloudinary.com
2. Install: `pip install django-cloudinary-storage`
3. Configure in settings.py

**Option 2: AWS S3**
1. Create S3 bucket
2. Install: `pip install django-storages boto3`
3. Configure in settings.py

### Database Backups
- PlanetScale: Automatic backups included
- Railway: Enable backups in settings
- Always backup before major changes

### Monitoring
- Check Render logs for errors
- Set up error monitoring (Sentry)
- Monitor database performance

---

## Environment Variables Reference

Copy this to your Render dashboard:

```
PYTHON_VERSION=3.12.0
DEBUG=False
SECRET_KEY=your-generated-secret-key-here
DB_NAME=your_mysql_database_name
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=your_mysql_host_url
DB_PORT=3306
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
```

---

## Next Steps After Deployment

1. ✅ Set up custom domain (optional)
2. ✅ Configure email backend for notifications
3. ✅ Set up SSL certificate (automatic on Render)
4. ✅ Enable database backups
5. ✅ Set up monitoring and alerts
6. ✅ Configure media storage (S3/Cloudinary)
7. ✅ Test payment gateway in production mode

---

## Support

If you encounter issues:
1. Check Render logs: Dashboard → Your Service → Logs
2. Check database connectivity
3. Verify all environment variables
4. Review Django error messages

Your app should now be live at: `https://your-app-name.onrender.com`

Good luck! 🚀
