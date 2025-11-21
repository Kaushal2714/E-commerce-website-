# 🚀 Deploy TrendMart to Vercel

## Quick Deployment Steps:

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from Project Directory
```bash
cd ecommerce_project
vercel
```

### 4. Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N**
- Project name? **trendmart** (or your choice)
- Directory? **.** (current directory)
- Override settings? **N**

### 5. After First Deployment, Run:
```bash
vercel --prod
```

---

## ⚠️ Important Notes:

### Database Limitation
- **Vercel doesn't support SQLite in production** (files are read-only)
- For production, you need to use a cloud database

### Recommended Solutions:

#### Option 1: Use Railway (Easiest for Django)
1. Go to https://railway.app
2. Create new project
3. Deploy from GitHub
4. Railway supports SQLite and file uploads
5. Free tier available

#### Option 2: Use PostgreSQL (Professional)
1. Get free PostgreSQL from:
   - **Neon** (https://neon.tech) - Free tier
   - **Supabase** (https://supabase.com) - Free tier
   - **ElephantSQL** (https://elephantsql.com) - Free tier

2. Update settings.py:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://user:pass@host:5432/dbname',
        conn_max_age=600
    )
}
```

3. Add to requirements.txt:
```
psycopg2-binary==2.9.9
dj-database-url==2.1.0
```

#### Option 3: Use PythonAnywhere (Best for Beginners)
1. Go to https://pythonanywhere.com
2. Free tier includes SQLite support
3. Upload your project
4. Configure web app
5. Media files work perfectly

---

## 📦 Alternative: Deploy to Railway (Recommended)

Railway is better for Django projects with SQLite:

### Steps:
1. Create account at https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Connect your GitHub repository
4. Railway auto-detects Django
5. Add environment variables if needed
6. Deploy! ✅

### Why Railway?
- ✅ Supports SQLite
- ✅ Supports media file uploads
- ✅ Easy Django deployment
- ✅ Free tier available
- ✅ Automatic HTTPS

---

## 🔧 For Vercel with PostgreSQL:

1. Get PostgreSQL URL from Neon/Supabase
2. Add to Vercel environment variables:
   ```
   DATABASE_URL=postgresql://...
   ```
3. Update requirements.txt (add psycopg2-binary)
4. Redeploy

---

## 📝 Environment Variables (if needed):

In Vercel dashboard, add:
- `SECRET_KEY` = your-secret-key
- `DEBUG` = False
- `DATABASE_URL` = your-database-url (if using PostgreSQL)

---

## 🎯 My Recommendation:

**For this project, use Railway or PythonAnywhere** because:
1. They support SQLite out of the box
2. Media file uploads work perfectly
3. Easier setup for Django
4. Free tier available

Vercel is great for Next.js/React, but Django works better on Railway/PythonAnywhere!
