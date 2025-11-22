from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser for admin access'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin123'
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists'))
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Password updated for user "{username}"'))
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
        
        self.stdout.write(self.style.SUCCESS('\n=== Admin Credentials ==='))
        self.stdout.write(self.style.SUCCESS(f'Username: {username}'))
        self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
        self.stdout.write(self.style.SUCCESS('========================\n'))
