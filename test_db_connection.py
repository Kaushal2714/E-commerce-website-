#!/usr/bin/env python
"""
Test database connection for debugging
Run this in Render shell to test DB connectivity
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.db import connection
from django.conf import settings

print("=" * 50)
print("DATABASE CONNECTION TEST")
print("=" * 50)

print("\n1. Database Configuration:")
print(f"   Engine: {settings.DATABASES['default']['ENGINE']}")
print(f"   Name: {settings.DATABASES['default']['NAME']}")
print(f"   User: {settings.DATABASES['default']['USER']}")
print(f"   Host: {settings.DATABASES['default']['HOST']}")
print(f"   Port: {settings.DATABASES['default']['PORT']}")

print("\n2. Testing Connection...")
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"   ✓ Connection successful! Result: {result}")
        
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"   ✓ MySQL Version: {version[0]}")
        
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        print(f"   ✓ Current Database: {db_name[0]}")
        
except Exception as e:
    print(f"   ✗ Connection failed!")
    print(f"   Error: {str(e)}")
    print(f"   Error Type: {type(e).__name__}")
    sys.exit(1)

print("\n3. Checking Tables...")
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print(f"   ✓ Found {len(tables)} tables:")
            for table in tables[:5]:  # Show first 5 tables
                print(f"     - {table[0]}")
        else:
            print("   ⚠ No tables found. Run migrations!")
except Exception as e:
    print(f"   ✗ Error checking tables: {str(e)}")

print("\n" + "=" * 50)
print("TEST COMPLETE")
print("=" * 50)
