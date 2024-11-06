from django.core.management import BaseCommand

from materials.models import Course
from users.models import User
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@example.com')
        user.set_password('123456')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
