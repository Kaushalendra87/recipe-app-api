from django.core.management.base import BaseCommand
import time
import psycopg2
from psycopg2 import OperationalError
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                psycopg2.connect(
                    dbname=settings.DATABASES["default"]["NAME"],
                    user=settings.DATABASES["default"]["USER"],
                    password=settings.DATABASES["default"]["PASSWORD"],
                    host=settings.DATABASES["default"]["HOST"],
                    port=5432,
                )
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))