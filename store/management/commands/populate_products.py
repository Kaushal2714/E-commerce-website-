from django.core.management.base import BaseCommand
from store.models import Category, Product
import os

class Command(BaseCommand):
    help = 'Populate database with products from images'

    def handle(self, *args, **kwargs):
        # Create categories
        categories_data = {
            'Electronics': 'Latest electronic gadgets and devices',
            'Fashion': 'Trendy clothing and accessories',
            'Sports': 'Sports equipment and gear',
            'Beauty': 'Beauty and personal care products'
        }
        
        categories = {}
        for name, desc in categories_data.items():
            cat, created = Category.objects.get_or_create(
                name=name,
                slug=name.lower(),
                defaults={'description': desc}
            )
            categories[name] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))
        
        # Product data based on your images
        products_data = [
            # Electronics
            {'name': 'Premium Laptop', 'category': 'Electronics', 'image': 'laptop1.jpg', 'price': 899.99, 'stock': 15, 
             'description': 'High-performance laptop with latest processor and stunning display'},
            {'name': 'Smartphone Pro', 'category': 'Electronics', 'image': 'phone1.jpg', 'price': 699.99, 'stock': 25,
             'description': 'Latest smartphone with advanced camera and 5G connectivity'},
            {'name': 'Smartphone Max', 'category': 'Electronics', 'image': 'phone2.jpg', 'price': 799.99, 'stock': 20,
             'description': 'Premium smartphone with exceptional battery life'},
            {'name': 'Smartphone Ultra', 'category': 'Electronics', 'image': 'phone3.jpg', 'price': 649.99, 'stock': 30,
             'description': 'Affordable flagship with amazing features'},
            {'name': 'Smartphone Plus', 'category': 'Electronics', 'image': 'phone4.jpg', 'price': 599.99, 'stock': 18,
             'description': 'Budget-friendly smartphone with great performance'},
            {'name': 'Smart TV 55"', 'category': 'Electronics', 'image': 'tv1.jpg', 'price': 549.99, 'stock': 10,
             'description': '4K Ultra HD Smart TV with HDR support'},
            {'name': 'Smart TV 65"', 'category': 'Electronics', 'image': 'tv2.jpg', 'price': 749.99, 'stock': 8,
             'description': 'Large screen 4K TV with smart features'},
            {'name': 'Gaming Headset', 'category': 'Electronics', 'image': 'hedset.jpg', 'price': 79.99, 'stock': 40,
             'description': 'Professional gaming headset with surround sound'},
            
            # Fashion - Jeans
            {'name': 'Classic Blue Jeans', 'category': 'Fashion', 'image': 'jeans1.jpg', 'price': 49.99, 'stock': 50,
             'description': 'Comfortable classic fit denim jeans'},
            {'name': 'Slim Fit Jeans', 'category': 'Fashion', 'image': 'jeans2.jpg', 'price': 54.99, 'stock': 45,
             'description': 'Modern slim fit jeans for everyday wear'},
            {'name': 'Distressed Jeans', 'category': 'Fashion', 'image': 'jeans3.jpg', 'price': 59.99, 'stock': 35,
             'description': 'Trendy distressed denim jeans'},
            {'name': 'Dark Wash Jeans', 'category': 'Fashion', 'image': 'jeans4.jpg', 'price': 52.99, 'stock': 40,
             'description': 'Premium dark wash denim jeans'},
            
            # Fashion - Shirts
            {'name': 'Casual Shirt', 'category': 'Fashion', 'image': 'shirt1.jpg', 'price': 29.99, 'stock': 60,
             'description': 'Comfortable casual shirt for daily wear'},
            {'name': 'Formal Shirt', 'category': 'Fashion', 'image': 'shirt2.jpg', 'price': 39.99, 'stock': 55,
             'description': 'Elegant formal shirt for office'},
            {'name': 'Designer Shirt', 'category': 'Fashion', 'image': 'srt3.jpg', 'price': 44.99, 'stock': 30,
             'description': 'Stylish designer shirt'},
            {'name': 'Premium Shirt', 'category': 'Fashion', 'image': 'shirt4.jpg', 'price': 49.99, 'stock': 25,
             'description': 'High-quality premium shirt'},
            
            # Fashion - T-Shirts
            {'name': 'Cotton T-Shirt', 'category': 'Fashion', 'image': 'tshirt1.jpg', 'price': 19.99, 'stock': 80,
             'description': 'Soft cotton t-shirt for casual wear'},
            {'name': 'Graphic T-Shirt', 'category': 'Fashion', 'image': 'tshirt3.jpg', 'price': 24.99, 'stock': 70,
             'description': 'Trendy graphic print t-shirt'},
            {'name': 'V-Neck T-Shirt', 'category': 'Fashion', 'image': 'tshirt4.jpg', 'price': 22.99, 'stock': 65,
             'description': 'Classic v-neck t-shirt'},
            
            # Fashion - Shoes
            {'name': 'Running Shoes', 'category': 'Fashion', 'image': 'shoes1.jpg', 'price': 79.99, 'stock': 35,
             'description': 'Comfortable running shoes with cushioning'},
            {'name': 'Casual Sneakers', 'category': 'Fashion', 'image': 'shoes2.jpg', 'price': 69.99, 'stock': 40,
             'description': 'Stylish casual sneakers for everyday'},
            {'name': 'Sport Shoes', 'category': 'Fashion', 'image': 'shoes4.jpg', 'price': 89.99, 'stock': 30,
             'description': 'Professional sport shoes'},
            
            # Sports
            {'name': 'Cricket Bat', 'category': 'Sports', 'image': 'bat.jpg', 'price': 59.99, 'stock': 20,
             'description': 'Professional cricket bat for players'},
            {'name': 'Football', 'category': 'Sports', 'image': 'ball.jpg', 'price': 24.99, 'stock': 50,
             'description': 'High-quality football for matches'},
            
            # Beauty
            {'name': 'Face Wash', 'category': 'Beauty', 'image': 'facewash.jpg', 'price': 12.99, 'stock': 100,
             'description': 'Gentle face wash for all skin types'},
        ]
        
        created_count = 0
        for product_data in products_data:
            category = categories[product_data['category']]
            slug = product_data['name'].lower().replace(' ', '-').replace('"', '').replace("'", '')
            
            product, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': product_data['name'],
                    'category': category,
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'image': f"products/{product_data['image']}",
                    'stock': product_data['stock'],
                    'available': True
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nTotal products created: {created_count}'))
