# E-Commerce Django Project

A simple e-commerce website built with Django.

## Features

- Product catalog with categories
- Shopping cart functionality
- User authentication
- Order management
- Admin panel for managing products

## Requirements

- Python 3.12+
- Django 5.2.5
- Pillow (for image handling)

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ecommerce_project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Create admin user**
```bash
python manage.py create_admin
```
This will create an admin user with:
- Username: `admin`
- Password: `admin123`

5. **Populate products (optional)**
```bash
python manage.py populate_products
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
ecommerce_project/
├── ecommerce_project/     # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py           # URL configuration
│   └── wsgi.py           # WSGI configuration
├── store/                # Store app
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # App URLs
│   ├── admin.py          # Admin configuration
│   ├── forms.py          # Forms
│   ├── templates/        # HTML templates
│   └── management/       # Custom management commands
├── media/                # User uploaded files
│   └── products/         # Product images
├── staticfiles/          # Collected static files
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Admin Credentials

**Username:** admin  
**Password:** admin123

*Note: Change this password in production!*

## Management Commands

- `python manage.py create_admin` - Create/reset admin user
- `python manage.py populate_products` - Populate database with sample products
- `python manage.py collectstatic` - Collect static files

## Development

To make changes:

1. Edit the code
2. Run migrations if you changed models:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Test your changes locally
4. Commit and push to Git

## License

This project is for educational purposes.
