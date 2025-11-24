from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Load sample products into the database'

    def handle(self, *args, **options):
        # Check if products already exist
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING('Products already exist. Skipping...'))
            return

        # Create categories if they don't exist
        electronics, _ = Category.objects.get_or_create(
            slug='electronics',
            defaults={
                'name': 'Electronics',
                'description': 'Latest electronic gadgets and devices'
            }
        )
        
        fashion, _ = Category.objects.get_or_create(
            slug='fashion',
            defaults={
                'name': 'Fashion',
                'description': 'Trendy clothing and accessories'
            }
        )
        
        sports, _ = Category.objects.get_or_create(
            slug='sports',
            defaults={
                'name': 'Sports',
                'description': 'Sports equipment and gear'
            }
        )
        
        beauty, _ = Category.objects.get_or_create(
            slug='beauty',
            defaults={
                'name': 'Beauty',
                'description': 'Beauty and personal care products'
            }
        )

        # Sample products
        products = [
            {
                'category': electronics,
                'name': 'Premium Laptop',
                'slug': 'premium-laptop',
                'description': 'High-performance laptop with latest processor and stunning display',
                'price': 89999.00,
                'stock': 15,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Smartphone Pro',
                'slug': 'smartphone-pro',
                'description': 'Latest smartphone with amazing camera and long battery life',
                'price': 79999.00,
                'stock': 25,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Wireless Headset',
                'slug': 'wireless-headset',
                'description': 'Premium wireless headset with noise cancellation',
                'price': 5999.00,
                'stock': 35,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Smart TV 55 inch',
                'slug': 'smart-tv-55',
                'description': '4K Ultra HD Smart TV with HDR',
                'price': 54999.00,
                'stock': 10,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Designer T-Shirt',
                'slug': 'designer-tshirt',
                'description': 'Premium quality cotton t-shirt with trendy design',
                'price': 1999.00,
                'stock': 50,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Denim Jeans',
                'slug': 'denim-jeans',
                'description': 'Comfortable and stylish denim jeans for everyday wear',
                'price': 2999.00,
                'stock': 40,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Casual Shirt',
                'slug': 'casual-shirt',
                'description': 'Comfortable casual shirt for daily wear',
                'price': 1499.00,
                'stock': 45,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Sports Shoes',
                'slug': 'sports-shoes',
                'description': 'Comfortable sports shoes for running and gym',
                'price': 3999.00,
                'stock': 30,
                'available': True
            },
            {
                'category': sports,
                'name': 'Cricket Bat',
                'slug': 'cricket-bat',
                'description': 'Professional cricket bat made from premium willow',
                'price': 4999.00,
                'stock': 20,
                'available': True
            },
            {
                'category': sports,
                'name': 'Football',
                'slug': 'football',
                'description': 'High-quality football for professional matches',
                'price': 1499.00,
                'stock': 30,
                'available': True
            },
            {
                'category': beauty,
                'name': 'Face Wash',
                'slug': 'face-wash',
                'description': 'Gentle face wash for all skin types',
                'price': 499.00,
                'stock': 100,
                'available': True
            },
        ]

        # Create products
        created_count = 0
        for product_data in products:
            Product.objects.create(**product_data)
            created_count += 1
            self.stdout.write(f'Created: {product_data["name"]}')

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} products!'))
        self.stdout.write(self.style.WARNING('Note: Products have no images. Add images through admin panel.'))
