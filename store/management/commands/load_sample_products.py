from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Load 30+ sample products into the database'

    def handle(self, *args, **options):
        # Check if products already exist
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING('Products already exist. Deleting and recreating...'))
            Product.objects.all().delete()

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

        # 30+ Sample products
        products = [
            # Electronics (12 products)
            {
                'category': electronics,
                'name': 'Premium Laptop Dell XPS',
                'slug': 'premium-laptop-dell-xps',
                'description': 'High-performance laptop with Intel i7 processor, 16GB RAM, 512GB SSD. Perfect for professionals and gamers.',
                'price': 89999.00,
                'stock': 15,
                'available': True
            },
            {
                'category': electronics,
                'name': 'iPhone 14 Pro Max',
                'slug': 'iphone-14-pro-max',
                'description': 'Latest iPhone with A16 Bionic chip, 256GB storage, ProMotion display, and advanced camera system.',
                'price': 129999.00,
                'stock': 25,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Samsung Galaxy S23 Ultra',
                'slug': 'samsung-galaxy-s23-ultra',
                'description': '5G smartphone with 200MP camera, S Pen, 12GB RAM, and stunning AMOLED display.',
                'price': 119999.00,
                'stock': 20,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Sony WH-1000XM5 Headphones',
                'slug': 'sony-wh1000xm5-headphones',
                'description': 'Industry-leading noise cancellation, premium sound quality, 30-hour battery life.',
                'price': 29999.00,
                'stock': 35,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Apple AirPods Pro 2',
                'slug': 'apple-airpods-pro-2',
                'description': 'Active noise cancellation, adaptive transparency, personalized spatial audio.',
                'price': 24999.00,
                'stock': 40,
                'available': True
            },
            {
                'category': electronics,
                'name': 'LG 55" 4K OLED TV',
                'slug': 'lg-55-4k-oled-tv',
                'description': 'Stunning 4K OLED display with Dolby Vision, perfect blacks, and vibrant colors.',
                'price': 89999.00,
                'stock': 10,
                'available': True
            },
            {
                'category': electronics,
                'name': 'iPad Air 5th Gen',
                'slug': 'ipad-air-5th-gen',
                'description': 'M1 chip, 10.9-inch Liquid Retina display, 256GB storage, perfect for creativity.',
                'price': 64999.00,
                'stock': 18,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Canon EOS R6 Camera',
                'slug': 'canon-eos-r6-camera',
                'description': 'Professional mirrorless camera with 20MP sensor, 4K video, and advanced autofocus.',
                'price': 219999.00,
                'stock': 8,
                'available': True
            },
            {
                'category': electronics,
                'name': 'PlayStation 5 Console',
                'slug': 'playstation-5-console',
                'description': 'Next-gen gaming console with ultra-fast SSD, ray tracing, and 4K gaming.',
                'price': 49999.00,
                'stock': 12,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Apple Watch Series 9',
                'slug': 'apple-watch-series-9',
                'description': 'Advanced health features, always-on display, fitness tracking, and seamless iPhone integration.',
                'price': 44999.00,
                'stock': 30,
                'available': True
            },
            {
                'category': electronics,
                'name': 'JBL Flip 6 Bluetooth Speaker',
                'slug': 'jbl-flip-6-speaker',
                'description': 'Portable waterproof speaker with powerful sound and 12-hour battery life.',
                'price': 9999.00,
                'stock': 45,
                'available': True
            },
            {
                'category': electronics,
                'name': 'Kindle Paperwhite',
                'slug': 'kindle-paperwhite',
                'description': 'Waterproof e-reader with 6.8" display, adjustable warm light, and weeks of battery life.',
                'price': 13999.00,
                'stock': 50,
                'available': True
            },

            # Fashion (10 products)
            {
                'category': fashion,
                'name': 'Levi\'s 501 Original Jeans',
                'slug': 'levis-501-original-jeans',
                'description': 'Classic straight fit jeans, 100% cotton denim, timeless style for everyday wear.',
                'price': 3999.00,
                'stock': 60,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Nike Air Max Sneakers',
                'slug': 'nike-air-max-sneakers',
                'description': 'Iconic sneakers with visible Air cushioning, comfortable and stylish for daily wear.',
                'price': 8999.00,
                'stock': 40,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Adidas Originals T-Shirt',
                'slug': 'adidas-originals-tshirt',
                'description': 'Classic cotton t-shirt with iconic trefoil logo, comfortable fit.',
                'price': 1999.00,
                'stock': 80,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Zara Formal Shirt',
                'slug': 'zara-formal-shirt',
                'description': 'Premium cotton formal shirt, perfect for office and formal occasions.',
                'price': 2499.00,
                'stock': 50,
                'available': True
            },
            {
                'category': fashion,
                'name': 'H&M Casual Hoodie',
                'slug': 'hm-casual-hoodie',
                'description': 'Comfortable cotton-blend hoodie with kangaroo pocket, perfect for casual wear.',
                'price': 2999.00,
                'stock': 45,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Puma Track Pants',
                'slug': 'puma-track-pants',
                'description': 'Comfortable track pants with elastic waistband, ideal for sports and lounging.',
                'price': 2499.00,
                'stock': 55,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Ray-Ban Aviator Sunglasses',
                'slug': 'rayban-aviator-sunglasses',
                'description': 'Classic aviator sunglasses with UV protection and iconic design.',
                'price': 7999.00,
                'stock': 35,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Leather Wallet',
                'slug': 'leather-wallet',
                'description': 'Genuine leather wallet with multiple card slots and bill compartment.',
                'price': 1499.00,
                'stock': 70,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Winter Jacket',
                'slug': 'winter-jacket',
                'description': 'Warm and stylish winter jacket with hood, perfect for cold weather.',
                'price': 4999.00,
                'stock': 30,
                'available': True
            },
            {
                'category': fashion,
                'name': 'Formal Blazer',
                'slug': 'formal-blazer',
                'description': 'Premium quality blazer for formal occasions and business meetings.',
                'price': 5999.00,
                'stock': 25,
                'available': True
            },

            # Sports (6 products)
            {
                'category': sports,
                'name': 'Professional Cricket Bat',
                'slug': 'professional-cricket-bat',
                'description': 'English willow cricket bat, perfect balance and power for serious players.',
                'price': 8999.00,
                'stock': 20,
                'available': True
            },
            {
                'category': sports,
                'name': 'FIFA Official Football',
                'slug': 'fifa-official-football',
                'description': 'FIFA approved match ball, perfect for professional games and practice.',
                'price': 2499.00,
                'stock': 40,
                'available': True
            },
            {
                'category': sports,
                'name': 'Badminton Racket Set',
                'slug': 'badminton-racket-set',
                'description': 'Professional badminton racket set with shuttlecocks and carry bag.',
                'price': 3999.00,
                'stock': 30,
                'available': True
            },
            {
                'category': sports,
                'name': 'Yoga Mat Premium',
                'slug': 'yoga-mat-premium',
                'description': 'Non-slip yoga mat with extra cushioning, perfect for yoga and fitness.',
                'price': 1999.00,
                'stock': 60,
                'available': True
            },
            {
                'category': sports,
                'name': 'Gym Dumbbell Set',
                'slug': 'gym-dumbbell-set',
                'description': 'Adjustable dumbbell set 5-25kg, perfect for home gym workouts.',
                'price': 6999.00,
                'stock': 25,
                'available': True
            },
            {
                'category': sports,
                'name': 'Tennis Racket Wilson',
                'slug': 'tennis-racket-wilson',
                'description': 'Professional tennis racket with graphite frame, excellent control and power.',
                'price': 7999.00,
                'stock': 18,
                'available': True
            },

            # Beauty (6 products)
            {
                'category': beauty,
                'name': 'Lakme Face Wash',
                'slug': 'lakme-face-wash',
                'description': 'Gentle face wash for all skin types, removes dirt and oil effectively.',
                'price': 299.00,
                'stock': 150,
                'available': True
            },
            {
                'category': beauty,
                'name': 'Maybelline Lipstick',
                'slug': 'maybelline-lipstick',
                'description': 'Long-lasting matte lipstick with rich color and smooth application.',
                'price': 499.00,
                'stock': 120,
                'available': True
            },
            {
                'category': beauty,
                'name': 'Nivea Body Lotion',
                'slug': 'nivea-body-lotion',
                'description': 'Moisturizing body lotion with vitamin E, keeps skin soft and hydrated.',
                'price': 399.00,
                'stock': 100,
                'available': True
            },
            {
                'category': beauty,
                'name': 'Dove Shampoo',
                'slug': 'dove-shampoo',
                'description': 'Nourishing shampoo for smooth and silky hair, suitable for daily use.',
                'price': 349.00,
                'stock': 130,
                'available': True
            },
            {
                'category': beauty,
                'name': 'Garnier Face Cream',
                'slug': 'garnier-face-cream',
                'description': 'Anti-aging face cream with SPF, reduces wrinkles and protects from sun.',
                'price': 599.00,
                'stock': 90,
                'available': True
            },
            {
                'category': beauty,
                'name': 'Himalaya Face Pack',
                'slug': 'himalaya-face-pack',
                'description': 'Natural face pack with neem and turmeric, purifies and brightens skin.',
                'price': 199.00,
                'stock': 140,
                'available': True
            },
        ]

        # Create products
        created_count = 0
        for product_data in products:
            Product.objects.create(**product_data)
            created_count += 1
            self.stdout.write(f'✓ Created: {product_data["name"]}')

        self.stdout.write(self.style.SUCCESS(f'\n🎉 Successfully created {created_count} products!'))
        self.stdout.write(self.style.SUCCESS('✓ Categories: Electronics, Fashion, Sports, Beauty'))
        self.stdout.write(self.style.WARNING('⚠ Note: Products have no images. They will show placeholder images.'))
