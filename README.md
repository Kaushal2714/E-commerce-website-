# 🛒 TrendMart - E-Commerce Website

A complete e-commerce website built with Django, featuring product management, shopping cart, payment integration, and user authentication.

---

## 📋 Table of Contents

1. [Features](#features)
2. [Quick Start](#quick-start)
3. [Installation](#installation)
4. [Database Setup](#database-setup)
5. [Payment Integration](#payment-integration)
6. [User Guide](#user-guide)
7. [Admin Panel](#admin-panel)
8. [Testing](#testing)
9. [Project Structure](#project-structure)
10. [Troubleshooting](#troubleshooting)

---

## ✨ Features

### Core Features
- ✅ **Product Catalog** - Browse products by categories
- ✅ **Search Functionality** - Search products by name, description, or category
- ✅ **Shopping Cart** - Add, update, remove items
- ✅ **User Authentication** - Register, login, logout
- ✅ **Order Management** - Place and track orders
- ✅ **Address Management** - Save and reuse delivery addresses
- ✅ **Payment Integration** - Razorpay (Online) & Cash on Delivery
- ✅ **Indian Currency** - All prices in ₹ (Rupees)
- ✅ **Responsive Design** - Works on all devices

### User Features
- 👤 User name display in navbar
- 🔍 Real-time product search
- 🛒 Persistent shopping cart
- 📍 Save multiple addresses
- 💳 Multiple payment options
- 📦 Order history and tracking
- ✉️ Success messages and notifications

### Admin Features
- 📊 Product management
- 📁 Category management
- 👥 User management
- 📦 Order management
- 📍 Address management
- 📈 Inventory tracking

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database
```bash
python manage.py migrate
python manage.py create_admin
python manage.py populate_products
```

### 3. Run Server
```bash
python manage.py runserver
```

### 4. Access Application
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

---

## 📦 Installation

### Requirements
- Python 3.12+
- MySQL (optional, SQLite by default)
- pip

### Step-by-Step Installation

#### 1. Clone Repository
```bash
git clone <your-repo-url>
cd ecommerce_project
```pts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

**Packages Installed:**
- Django 5.2.5
- Pillow 10.4.0 (Image handling)
- mysqlclient 2.2.0 (MySQL support)
- razorpay 1.4.2 (Payment gateway)

4. **Run Migrations**
```bash
python manage.py migrate
```

5. **Create Admin & Load Data**
```bash
python manage.py create_admin
python manage.py populate_products
```

6. **Start Server**
```bash
python manage.py runserver
```

---

## 🗄️ Database Setup

### Option 1: SQLite (Default - Recommended for Development)

**Already configured!** No additional setup needed.

**Database File:** `db.sqlite3`

### Option 2: MySQL (For Production)

#### Step 1: Install MySQL
Download from: https://dev.mysql.com/downloads/mysql/

#### Step 2: Create Database
```sql
CREATE DATABASE ecommerce_data CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### Step 3: Update Settings
Edit `ecommerce_project/settings.py`:

```python
# Comment out SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Uncomment MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_data',
        'USER': 'root',
        'PASSWORD': 'your_password',  # Change this
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```

#### Step 4: Run Migrations
```bash
python manage.py migrate
python manage.py create_admin
python manage.py populate_products
```

---

## 👤 Admin Access

### Default Admin Credentials
- **Username:** `admin`
- **Password:** `admin123`

### Admin Panel Features
- **Products** - Add, edit, delete products
- **Categories** - Manage product categories
- **Orders** - View and manage orders
- **Addresses** - View customer addresses
- **Users** - Manage user accounts

### Change Admin Password
```bash
python manage.py changepassword admin
```

---

## 💳 Payment Integration

### Razorpay Setup

#### Step 1: Create Razorpay Account
1. Visit: https://razorpay.com/
2. Sign up (Free)
3. Verify email and phone

#### Step 2: Get API Keys
1. Login to Razorpay Dashboard
2. Go to **Settings** → **API Keys**
3. Click **Generate Test Keys**
4. Copy:
   - Key ID (starts with `rzp_test_`)
   - Key Secret

#### Step 3: Update Settings
Edit `ecommerce_project/settings.py`:

```python
# Razorpay Payment Gateway Settings
RAZORPAY_KEY_ID = 'rzp_test_YOUR_KEY_ID'  # Replace
RAZORPAY_KEY_SECRET = 'YOUR_KEY_SECRET'    # Replace
```

#### Step 4: Test Payment
Use test card details:
- **Card Number:** 4111 1111 1111 1111
- **CVV:** Any 3 digits
- **Expiry:** Any future date

### Payment Methods Available
1. **Razorpay (Online)**
   - Credit/Debit Cards
   - UPI (Google Pay, PhonePe, Paytm)
   - Net Banking
   - Wallets

2. **Cash on Delivery (COD)**
   - Pay when you receive the product

---

## 📖 User Guide

### For Customers

#### 1. Registration
1. Click **Register** in navbar
2. Fill registration form
3. Click **Register**
4. Automatically logged in

#### 2. Login
1. Click **Login** in navbar
2. Enter username and password
3. Click **Login**
4. See your name in navbar: 👤 [Your Name]

#### 3. Browse Products
1. View all products on homepage
2. Click category buttons to filter
3. Use search bar to find products
4. Click product to see details

#### 4. Search Products
1. Use search bar at top
2. Type product name, category, or description
3. Results appear instantly
4. Click "Clear Search" to see all products

**Search Examples:**
- "phone" → Shows all smartphones
- "laptop" → Shows laptops
- "jeans" → Shows jeans
- "electronics" → Shows electronics category

#### 5. Add to Cart
1. Click **Add to Cart** on product
2. See success message
3. Click **🛒 Cart** to view cart
4. Update quantities with +/- buttons
5. Remove items if needed

#### 6. Checkout Process

**First Time:**
1. Click **Proceed to Checkout**
2. Fill complete address form:
   - Full Name
   - Phone Number (10 digits)
   - Address Line 1 & 2
   - City, State, Pincode
3. Check **"Save this address"** (optional)
4. Select payment method:
   - 💳 Pay with Razorpay
   - 💵 Cash on Delivery
5. Click **Proceed to Payment** or **Place Order**

**Next Time:**
1. Click **Proceed to Checkout**
2. Select saved address from dropdown
3. Form auto-fills!
4. Select payment method
5. Complete order

#### 7. View Orders
1. Click **My Orders** in navbar
2. See all your orders
3. Click **View Details** for order info
4. Check order status

#### 8. Logout
1. Click **Logout** in navbar
2. See success message
3. Redirected to login page

---

## 🧪 Testing

### Quick Test (5 Minutes)

#### Test 1: Login/Logout
```bash
python manage.py runserver
```
1. Visit: http://127.0.0.1:8000/
2. Click **Login**
3. Enter: `admin` / `admin123`
4. ✅ Should see: "Welcome back, admin!"
5. ✅ Should see: 👤 admin in navbar
6. Click **Logout**
7. ✅ Should see: "You have been logged out successfully!"
8. ✅ Should be on login page

#### Test 2: Search
1. Login
2. Search "phone"
3. ✅ Should show smartphones
4. Search "laptop"
5. ✅ Should show laptops

#### Test 3: Shopping Cart
1. Click **Add to Cart** on any product
2. ✅ Should see success message
3. Click **🛒 Cart**
4. ✅ Should see your items
5. Change quantity
6. ✅ Price should update

#### Test 4: Checkout with Address
1. In cart, click **Proceed to Checkout**
2. Fill address:
   ```
   Name: John Doe
   Phone: 9876543210
   Address: 123, MG Road
   City: Mumbai
   State: Maharashtra
   Pincode: 400001
   ```
3. Check **"Save this address"**
4. Select **Cash on Delivery**
5. Click **Place Order**
6. ✅ Should see: "Order placed successfully!"

#### Test 5: Saved Address
1. Add products to cart again
2. Go to checkout
3. ✅ Should see saved address dropdown
4. Select your address
5. ✅ Form should auto-fill
6. Complete order

#### Test 6: View Orders
1. Click **My Orders**
2. ✅ Should see your orders
3. Click **View Details**
4. ✅ Should see order info

### Test Checklist
- [ ] Login works
- [ ] Logout redirects to login
- [ ] User name shows in navbar
- [ ] Search finds products
- [ ] Add to cart works
- [ ] Cart updates correctly
- [ ] Address form appears
- [ ] Save address works
- [ ] Saved address loads
- [ ] COD payment works
- [ ] Order created
- [ ] Order details show
- [ ] All prices in ₹

---

## 📁 Project Structure

```
ecommerce_project/
├── ecommerce_project/          # Main project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── store/                     # E-commerce app
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   ├── forms.py               # Forms
│   │
│   ├── templates/store/       # HTML templates
│   │   ├── base.html          # Base template
│   │   ├── product_list.html  # Products page
│   │   ├── product_detail.html # Product details
│   │   ├── cart.html          # Shopping cart
│   │   ├── checkout.html      # Checkout page
│   │   ├── order_list.html    # Orders list
│   │   ├── order_detail.html  # Order details
│   │   ├── login.html         # Login page
│   │   └── register.html      # Registration page
│   │
│   └── management/commands/   # Custom commands
│       ├── create_admin.py    # Create admin user
│       └── populate_products.py # Load sample products
│
├── media/products/            # Product images (25 images)
├── staticfiles/               # Collected static files
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### Database Models

#### Category
- name, slug, description

#### Product
- name, slug, description, price, image, stock, available, category

#### Address
- user, full_name, phone, address_line1, address_line2, city, state, pincode, is_default

#### Cart & CartItem
- Shopping cart functionality

#### Order & OrderItem
- Order management with payment tracking

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Server Won't Start
**Error:** Port already in use
```bash
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID [PID_NUMBER] /F
```

#### 2. Database Errors
**Error:** No such table
```bash
python manage.py migrate
```

**Error:** MySQL connection failed
- Check MySQL is running
- Verify credentials in settings.py
- Check database exists

#### 3. Static Files Not Loading
```bash
python manage.py collectstatic
```

#### 4. Images Not Showing
- Check `media/products/` folder exists
- Verify images are present
- Check file permissions

#### 5. Login Not Working
**Reset admin password:**
```bash
python manage.py create_admin
```

#### 6. Search Not Working
- Check products exist in database
- Verify search query is being passed
- Check browser console for errors

#### 7. Payment Popup Not Opening
- Verify Razorpay keys are correct
- Check browser console for errors
- Try different browser

#### 8. Address Not Saving
- Check "Save this address" is checked
- Verify all required fields filled
- Check database connection

### Debug Mode

To see detailed errors, ensure in `settings.py`:
```python
DEBUG = True
```

**Note:** Set to `False` in production!

---

## 🔐 Security Notes

### For Development
✅ DEBUG = True (shows detailed errors)
✅ SQLite database (simple setup)
✅ Test Razorpay keys (no real money)

### For Production
⚠️ Set DEBUG = False
⚠️ Use MySQL/PostgreSQL
⚠️ Use Live Razorpay keys
⚠️ Enable HTTPS
⚠️ Use environment variables for secrets
⚠️ Change admin password
⚠️ Set strong SECRET_KEY

---

## 📊 Database Information

### Current Setup
- **Database:** SQLite (db.sqlite3)
- **Location:** Project root
- **Size:** ~500KB with sample data

### Tables Created
- auth_user (Users)
- store_category (4 categories)
- store_product (25 products)
- store_address (User addresses)
- store_cart (Shopping carts)
- store_cartitem (Cart items)
- store_order (Orders)
- store_orderitem (Order items)

### Sample Data
- **Categories:** 4 (Electronics, Fashion, Sports, Beauty)
- **Products:** 25 items with images
- **Admin User:** 1 (admin/admin123)

---

## 🎨 Customization

### Change Colors
Edit `store/templates/store/base.html`:
```css
/* Main gradient colors */
background: linear-gradient(135deg, #ff9a56 0%, #ff6b35 100%);

/* Change to your colors */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

### Add More Products
1. Go to admin panel
2. Click **Products** → **Add Product**
3. Fill details and upload image
4. Save

### Add More Categories
1. Go to admin panel
2. Click **Categories** → **Add Category**
3. Enter name and slug
4. Save

### Modify Prices
1. Go to admin panel
2. Click **Products**
3. Edit price directly in list
4. Save

---

## 📞 Support & Resources

### Django Documentation
- Official Docs: https://docs.djangoproject.com/
- Tutorial: https://docs.djangoproject.com/en/5.2/intro/tutorial01/

### Razorpay Documentation
- Docs: https://razorpay.com/docs/
- Test Cards: https://razorpay.com/docs/payments/payments/test-card-details/
- Support: support@razorpay.com

### MySQL Documentation
- Docs: https://dev.mysql.com/doc/
- Download: https://dev.mysql.com/downloads/mysql/

---

## 🎯 Features Summary

### ✅ Completed Features
1. **User Management**
   - Registration & Login
   - Logout with redirect
   - User name display in navbar
   - Session management

2. **Product Management**
   - Product catalog
   - Category filtering
   - Product details
   - Image display
   - Stock management

3. **Search Functionality**
   - Search by name
   - Search by description
   - Search by category
   - Instant results
   - Clear search option

4. **Shopping Cart**
   - Add to cart
   - Remove from cart
   - Update quantities
   - Cart total calculation
   - Empty cart handling

5. **Address Management**
   - Complete address form
   - Save addresses
   - Reuse saved addresses
   - Auto-fill form
   - Indian states dropdown
   - Phone & pincode validation

6. **Payment Integration**
   - Razorpay online payment
   - Cash on Delivery
   - Payment tracking
   - Test mode support

7. **Order Management**
   - Place orders
   - View order history
   - Order details
   - Order status tracking
   - Payment method tracking

8. **Currency**
   - Indian Rupees (₹)
   - Proper formatting
   - Consistent display

9. **Admin Panel**
   - Product management
   - Category management
   - Order management
   - Address management
   - User management

---

## 🚀 Next Steps

### Optional Enhancements
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Email notifications
- [ ] Order tracking
- [ ] Multiple product images
- [ ] Product variants (size, color)
- [ ] Discount coupons
- [ ] Inventory alerts
- [ ] Sales reports
- [ ] Customer dashboard

---

## 📝 License

This project is for educational purposes.

---

## 🎉 Congratulations!

Your e-commerce website is ready to use!

**Quick Start:**
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

**Admin:** http://127.0.0.1:8000/admin/
- Username: `admin`
- Password: `admin123`

Happy Shopping! 🛒✨
lect saved address
- [ ] Form auto-fills
- [ ] Complete order

#### 7. Orders
- [ ] View order list
- [ ] See order details
- [ ] Check order status
- [ ] Verify address
- [ ] See payment method

#### 8. Admin Panel
- [ ] Login to admin
- [ ] Add product
- [ ] Edit product
- [ ] View orders
- [ ] Update order status
- [ ] View addresses

### Test Accounts

**Admin:**
- Username: `admin`
- Password: `admin123`

**Test Cards (Razorpay):**
- Success: `4111 1111 1111 1111`
- Success: `5555 5555 5555 4444`
- Failure: `4000 0000 0000 0002`

---

## 📁 Project Structure

```
ecommerce_project/
├── ecommerce_project/          # Main project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── store/                     # E-commerce app
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   ├── forms.py               # Forms
│   │
│   ├── templates/store/       # HTML templates
│   │   ├── base.html          # Base template
│   │   ├── product_list.html  # Products page
│   │   ├── product_detail.html # Product details
│   │   ├── cart.html          # Shopping cart
│   │   ├── checkout.html      # Checkout page
│   │   ├── order_list.html    # Orders list
│   │   ├── order_detail.html  # Order details
│   │   ├── login.html         # Login page
│   │   └── register.html      # Registration page
│   │
│   └── management/commands/   # Custom commands
│       ├── create_admin.py    # Create admin user
│       └── populate_products.py # Load sample products
│
├── media/                     # User uploaded files
│   └── products/              # Product images (25 images)
│
├── staticfiles/               # Collected static files
│
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── create_mysql_db.sql        # MySQL database script
└── README.md                  # This file
```

### Database Models

#### Category
- name (CharField)
- slug (SlugField)
- description (TextField)

#### Product
- category (ForeignKey)
- name (CharField)
- slug (SlugField)
- description (TextField)
- price (DecimalField)
- image (ImageField)
- stock (IntegerField)
- available (BooleanField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

#### Address
- user (ForeignKey)
- full_name (CharField)
- phone (CharField)
- address_line1 (CharField)
- address_line2 (CharField)
- city (CharField)
- state (CharField)
- pincode (CharField)
- is_default (BooleanField)
- created_at (DateTimeField)

#### Cart
- user (ForeignKey)
- created_at (DateTimeField)

#### CartItem
- cart (ForeignKey)
- product (ForeignKey)
- quantity (PositiveIntegerField)

#### Order
- user (ForeignKey)
- status (CharField)
- total_amount (DecimalField)
- shipping_address (TextField)
- address (ForeignKey)
- payment_method (CharField)
- payment_id (CharField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

#### OrderItem
- order (ForeignKey)
- product (ForeignKey)
- quantity (PositiveIntegerField)
- price (DecimalField)

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Server Won't Start
**Error:** `Port already in use`

**Solution:**
```bash
# Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:8000 | xargs kill -9
```

#### 2. Database Errors
**Error:** `no such table`

**Solution:**
```bash
python manage.py migrate
```

#### 3. Static Files Not Loading
**Error:** Images not showing

**Solution:**
```bash
python manage.py collectstatic
```

#### 4. Login Not Working
**Error:** Invalid credentials

**Solution:**
```bash
python manage.py create_admin
# Use: admin / admin123
```

#### 5. Payment Not Working
**Error:** Razorpay popup not opening

**Solution:**
- Check if API keys are set in settings.py
- Verify keys are correct
- Check browser console for errors
- Try different browser

#### 6. Search Not Working
**Error:** No results found

**Solution:**
- Check if products exist in database
- Run: `python manage.py populate_products`
- Verify search query

#### 7. Address Not Saving
**Error:** Address not in dropdown

**Solution:**
- Check "Save this address" checkbox
- Verify all required fields filled
- Check database connection

### Debug Mode

To see detailed errors, ensure in `settings.py`:
```python
DEBUG = True
```

**Note:** Set to `False` in production!

### Clear Cache

If issues persist:
```bash
# Clear browser cache
# Or use incognito/private mode

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## 🔒 Security Notes

### Important Security Practices

#### 1. Secret Key
**Current:** Visible in settings.py  
**Production:** Use environment variables

```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
```

#### 2. Debug Mode
**Development:** `DEBUG = True`  
**Production:** `DEBUG = False`

#### 3. Allowed Hosts
**Development:** `['127.0.0.1', 'localhost']`  
**Production:** Add your domain

```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

#### 4. Database Password
**Never commit:** Database passwords to Git  
**Use:** Environment variables

#### 5. Razorpay Keys
**Test Mode:** Use test keys (rzp_test_...)  
**Live Mode:** Use live keys (rzp_live_...)  
**Never commit:** API keys to Git

### HTTPS
Always use HTTPS in production for:
- Login/Registration
- Payment processing
- Sensitive data

---

## 📊 Features Summary

### Implemented Features

| Feature | Status | Description |
|---------|--------|-------------|
| Product Catalog | ✅ | Browse 25 products in 4 categories |
| Search | ✅ | Search by name, description, category |
| Shopping Cart | ✅ | Add, update, remove items |
| User Auth | ✅ | Register, login, logout |
| Address Management | ✅ | Save and reuse addresses |
| Payment Gateway | ✅ | Razorpay integration |
| COD | ✅ | Cash on Delivery option |
| Order Management | ✅ | Place and track orders |
| Admin Panel | ✅ | Manage products, orders, users |
| Indian Currency | ✅ | All prices in ₹ |
| Responsive Design | ✅ | Mobile-friendly |
| User Name Display | ✅ | Show logged-in user |
| Saved Addresses | ✅ | Quick address selection |
| Order History | ✅ | View past orders |
| Product Images | ✅ | 25 product images included |

### Database
- ✅ SQLite (Default)
- ✅ MySQL Support
- ✅ 7 Models
- ✅ Migrations included

### Payment
- ✅ Razorpay (Test Mode)
- ✅ Cash on Delivery
- ✅ Payment tracking
- ✅ Test cards supported

---

## 🚀 Going Live

### Production Checklist

#### Before Deployment:
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Use environment variables for secrets
- [ ] Switch to production database (MySQL/PostgreSQL)
- [ ] Get Razorpay live keys
- [ ] Complete Razorpay KYC
- [ ] Setup HTTPS
- [ ] Configure email backend
- [ ] Setup static files hosting
- [ ] Setup media files hosting (AWS S3/Cloudinary)
- [ ] Add error logging
- [ ] Setup backup system
- [ ] Test all features
- [ ] Load test the application

#### Deployment Options:
- Railway
- Heroku
- DigitalOcean
- AWS
- Google Cloud
- Azure

---

## 📞 Support

### Resources
- **Django Docs:** https://docs.djangoproject.com/
- **Razorpay Docs:** https://razorpay.com/docs/
- **MySQL Docs:** https://dev.mysql.com/doc/

### Contact
For issues or questions:
1. Check this README
2. Check Django documentation
3. Check error messages in terminal
4. Use browser console (F12) for frontend issues

---

## 📝 License

This project is for educational purposes.

---

## 🎉 Congratulations!

Your e-commerce website is ready to use!

**Quick Start:**
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

**Admin Login:**
- Username: `admin`
- Password: `admin123`

**Happy Selling!** 🛒✨
