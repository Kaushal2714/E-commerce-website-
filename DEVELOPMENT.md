# Development Guide

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Setup database:**
```bash
python manage.py migrate
python manage.py create_admin
python manage.py populate_products
```

3. **Run server:**
```bash
python manage.py runserver
```

4. **Access:**
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

## Common Tasks

### Add New Products
1. Go to admin panel
2. Click "Products" → "Add Product"
3. Fill in details and upload image
4. Save

### Create New Category
1. Go to admin panel
2. Click "Categories" → "Add Category"
3. Enter name and slug (lowercase, no spaces)
4. Save

### Reset Database
```bash
del db.sqlite3
python manage.py migrate
python manage.py create_admin
python manage.py populate_products
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## Project Models

### Category
- name: Category name
- slug: URL-friendly name
- description: Category description

### Product
- name: Product name
- slug: URL-friendly name
- category: Foreign key to Category
- description: Product description
- price: Decimal price
- image: Product image
- stock: Available quantity
- available: Boolean availability

### Cart & CartItem
- Shopping cart functionality
- Links to User and Products

### Order & OrderItem
- Order management
- Order status tracking
- Order history

## Tips

- Always run migrations after model changes
- Use `python manage.py shell` for testing queries
- Check admin panel for data management
- Media files are stored in `media/` folder
- Static files are collected to `staticfiles/` folder
