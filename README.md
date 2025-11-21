# Django E-Commerce Project

A complete e-commerce web application built with Django.

## Features

- Product catalog with categories
- Shopping cart functionality
- Order management system
- User authentication
- Admin panel for managing products, orders, and categories

## Setup Instructions

### 1. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 2. Run the development server
```bash
python manage.py runserver
```

### 3. Access the application
- Main store: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Admin Panel
1. Login to the admin panel at `/admin/`
2. Add categories (e.g., Electronics, Clothing, Books)
3. Add products with details like name, price, description, stock, and category

### Customer Features
1. Browse products on the homepage
2. Filter products by category
3. View product details
4. Add products to cart (requires login)
5. Update cart quantities
6. Checkout and place orders
7. View order history

## Models

- **Category**: Product categories
- **Product**: Product information (name, price, description, stock, image)
- **Cart**: Shopping cart for each user
- **CartItem**: Items in the cart
- **Order**: Customer orders
- **OrderItem**: Items in each order

## Project Structure

```
ecommerce_project/
├── ecommerce_project/     # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── store/                 # Main app
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin configuration
│   └── templates/        # HTML templates
├── media/                # Uploaded images
└── manage.py
```

## Next Steps

1. Create a superuser account
2. Add some categories and products via admin panel
3. Test the shopping flow
4. Customize the templates and styling as needed
