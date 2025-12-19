from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Initialize default users (admin, customer, manager) with groups"

    def handle(self, *args, **options):
        User = get_user_model()

        USERS = [
            {
                "username": "admin",
                "password": "admin",
                "is_staff": True,
                "is_superuser": True,
                "groups": ["manager"],
            },
            {
                "username": "customer",
                "password": "customer",
                "is_staff": False,
                "is_superuser": False,
                "groups": ["customer"],
            },
            {
                "username": "manager",
                "password": "manager",
                "is_staff": True,
                "is_superuser": False,
                "groups": ["manager"],
            },
        ]

        for u in USERS:
            # Create user if not exists
            if not User.objects.filter(username=u["username"]).exists():
                user = User.objects.create_user(
                    username=u["username"],
                    password=u["password"],
                    is_staff=u["is_staff"],
                    is_superuser=u["is_superuser"],
                )
                # Add user to groups
                for group_name in u["groups"]:
                    group, _ = Group.objects.get_or_create(name=group_name)
                    user.groups.add(group)
                self.stdout.write(self.style.SUCCESS(f"User {u['username']} created."))
            else:
                self.stdout.write(f"User {u['username']} already exists.")
