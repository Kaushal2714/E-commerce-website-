# 🚀 Quick Start - Deploy to Railway

## 5-Minute Deployment Guide

### Step 1: Push to GitHub (1 min)
```bash
git add .
git commit -m "Configure for Railway deployment"
git push origin master
```

### Step 2: Create Railway Project (2 min)

1. Go to https://railway.app
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository: `E-commerce-website-`
5. Click **"Add PostgreSQL"** database

### Step 3: Set Environment Variables (1 min)

In Railway Dashboard → Your Service → Variables:

1. Click **"New Variable"**
2. Add:
   ```
   SECRET_KEY = <paste-generated-key>
   DEBUG = False
   ```

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Deploy & Wait (1 min)

Railway will automatically:
- ✅ Install dependencies
- ✅ Run migrations
- ✅ Collect static files
- ✅ Copy media files
- ✅ Start server

Watch the logs for completion.

### Step 5: Create Admin User

1. In Railway → Your Service → Settings
2. Click **"Open Terminal"** or use Railway CLI
3. Run:
   ```bash
   python manage.py create_admin
   ```

**Credentials:**
- Username: `admin`
- Password: `admin123`

### Step 6: Access Your Site

1. Railway Dashboard → Settings → Networking
2. Click **"Generate Domain"**
3. Visit: `https://your-app.up.railway.app`
4. Admin: `https://your-app.up.railway.app/admin/`

---

## ✅ Verification

- [ ] Site loads without errors
- [ ] Product images are showing
- [ ] Admin panel is accessible
- [ ] Can login with admin/admin123
- [ ] Products are visible

---

## ⚠️ Important

**Change admin password immediately:**
1. Login to admin panel
2. Click "Users" → "admin"
3. Click "Change password"
4. Set a strong password

---

## 🆘 Issues?

### Build Failed
- Check Railway logs for errors
- Verify all files are committed
- Check requirements.txt syntax

### Static Files Not Loading
- Check logs for "collectstatic" success
- Verify WhiteNoise is installed
- Check STATIC_ROOT setting

### Database Error
- Ensure PostgreSQL is added
- Check DATABASE_URL is set
- Verify migrations ran

### Media Files Missing
- Check "copy_media_to_static" in logs
- Verify media files are in Git repo
- Check staticfiles/media/ exists

---

## 📚 Full Documentation

- **Complete Guide:** `RAILWAY_DEPLOYMENT.md`
- **Checklist:** `DEPLOYMENT_CHECKLIST.md`
- **Changes Report:** `DEPLOYMENT_CHANGES_REPORT.md`

---

## 🎉 Success!

Your e-commerce site is now live on Railway!

**Next Steps:**
1. Change admin password
2. Add your products
3. Customize the site
4. Share your URL!

---

**Need Help?** Check the full documentation files or Railway support.
