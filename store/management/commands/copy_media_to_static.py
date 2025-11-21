import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Copy media files to staticfiles directory for production serving'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        static_root = settings.STATIC_ROOT
        
        media_static_dir = os.path.join(static_root, 'media')
        os.makedirs(media_static_dir, exist_ok=True)
        
        if os.path.exists(media_root):
            for item in os.listdir(media_root):
                src = os.path.join(media_root, item)
                dst = os.path.join(media_static_dir, item)
                
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                    self.stdout.write(self.style.SUCCESS(f'Copied directory: {item}'))
                else:
                    shutil.copy2(src, dst)
                    self.stdout.write(self.style.SUCCESS(f'Copied file: {item}'))
        
        self.stdout.write(self.style.SUCCESS('Media files copied to static successfully!'))
