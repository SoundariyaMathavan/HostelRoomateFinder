from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_notification'),  # Updated to depend on the last applied migration
    ]

    operations = [
        # The is_paid field is already defined in the initial migration
        # This migration is now a no-op (no operation) to avoid conflicts
    ]