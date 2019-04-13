from django.core.management.base import BaseCommand
from users.tests.factories import CustomUserFactory
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()
CustomUser = get_user_model()


class Command(BaseCommand):
    help = "Delete all existing data and import fake data to populate the database"

    def create_admin_users(self):
        """Create and return an admin user"""
        admin_user = CustomUserFactory(
            email="admin@email.com",
            is_superuser=True,
            is_staff=True,
            life_motto="Even the tallest and most formidable of towers, was once just a pile of bricks. Stay Relentless",
        )
        admin_user.set_password("adminadmin")
        admin_user.save()

    def handle(self, *args, **kwargs):
        CustomUser.objects.all().delete()

        self.create_admin_users()
        print("\nAdmin user created.")
