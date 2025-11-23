# Troubleshooting Server Error (500)

## Most Common Causes:

### 1. Database Connection Issue (Most Likely)
Your MySQL database is not connected or credentials are wrong.

### 2. Missing Environment Variables
Required environment variables are not set in Render.

### 3. Database Not Migrated
Tables don't exist in the database.

---

## Step-by-Step Fix

### Step 1: Check Render Logs
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Look for error messages (usually red text)
5. **Share the error message to identify the exact issue**

Common errors you might see:
- `Can't connect to MySQL server`
- `Access denied for user`
- `Unknown database`
- `no such table`

---

### Step 2: Verify Environment Variables in Render

Go to Render Dashboard → Your Service → Environment

**Required Variables:**

```
DEBUG=False
SECRET_KEY=your-secret-key-here
DB_NAME=your_database_name
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=your_mysql_host
DB_PORT=3306
RAZORPAY_KEY_ID=your_key
RAZORPAY_KEY_SECRET=your_secret
```

**Important:** Make sure there are NO spaces around the `=` sign!

❌ Wrong: `DB_NAME = mydb`
✅ Correct: `DB_NAME=mydb`

---

### Step 3: Test Database Connection

In Render Dashboard → Your Service → Shell, run:

```bash
python test_db_connection.py
```

This will tell you exactly what's wrong with the database connection.

---

### Step 4: Common Database Issues & Solutions

#### Issue A: "Can't connect to MySQL server"
**Cause:** Wrong DB_HOST or database not accessible

**Solution:**
1. Verify your MySQL database is running
2. Check DB_HOST is correct (should be a URL, not localhost)
3. Ensure your MySQL service allows external connections
4. Check firewall rules

#### Issue B: "Access denied for user"
**Cause:** Wrong username or password

**Solution:**
1. Double-check DB_USER in Render matches your MySQL username
2. Double-check DB_PASSWORD (no extra spaces!)
3. Verify user has permissions on the database

#### Issue C: "Unknown database"
**Cause:** Database doesn't exist

**Solution:**
1. Create the database in your MySQL service
2. Make sure DB_NAME matches exactly (case-sensitive!)

#### Issue D: "no such table: store_product"
**Cause:** Migrations not run

**Solution:**
In Render Shell, run:
```bash
python manage.py migrate
```

---

### Step 5: Temporarily Enable DEBUG (For Testing Only)

To see the actual error on the website:

1. In Render Dashboard → Environment Variables
2. Change `DEBUG=False` to `DEBUG=True`
3. Save and redeploy
4. Visit your site - you'll see the detailed error
5. **IMPORTANT:** Change back to `DEBUG=False` after fixing!

---

## Quick Checklist

- [ ] MySQL database is created and running
- [ ] All environment variables are set in Render
- [ ] DB_HOST is the external MySQL host (not localhost)
- [ ] DB credentials are correct (no typos)
- [ ] Migrations have been run
- [ ] Build completed successfully
- [ ] No errors in Render logs

---

## If You Don't Have a MySQL Database Yet

### Option 1: PlanetScale (Free)
1. Go to https://planetscale.com
2. Sign up and create database
3. Get connection details
4. Use these in Render environment variables

### Option 2: Railway MySQL ($5/month)
1. Go to https://railway.app
2. New Project → Add MySQL
3. Get connection details from Variables tab
4. Use these in Render environment variables

### Option 3: Use SQLite for Testing (Quick Fix)

If you just want to test the deployment, temporarily use SQLite:

In Render Shell:
```bash
# This will use SQLite instead of MySQL
export DB_ENGINE=django.db.backends.sqlite3
python manage.py migrate
```

Then in Render Environment Variables, add:
```
DB_ENGINE=django.db.backends.sqlite3
```

**Note:** SQLite is NOT recommended for production!

---

## Still Getting 500 Error?

### Get the Exact Error:

1. In Render Shell, run:
```bash
python manage.py check
python manage.py check --deploy
```

2. Try to start the server manually:
```bash
python manage.py runserver 0.0.0.0:8000
```

3. Check if you can access Django shell:
```bash
python manage.py shell
```

Then in the shell:
```python
from django.db import connection
connection.ensure_connection()
print("Database connected!")
```

---

## Share These Details for Help:

If still stuck, share:
1. Error from Render Logs (the red text)
2. Output of `python test_db_connection.py`
3. Your database provider (PlanetScale, Railway, etc.)
4. Screenshot of your environment variables (hide passwords!)

---

## After Fixing:

Once working:
1. Set `DEBUG=False` in Render
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Test your site thoroughly

Good luck! 🚀
