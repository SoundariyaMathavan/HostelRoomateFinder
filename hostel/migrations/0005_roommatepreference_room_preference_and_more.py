# Generated by Django 5.1.7 on 2025-04-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommatepreference',
            name='room_preference',
            field=models.CharField(choices=[('quiet', 'Quiet Room'), ('social', 'Social Room'), ('balanced', 'Balanced')], default='balanced', max_length=20),
        ),
        migrations.AddField(
            model_name='roommatepreference',
            name='sharing_preference',
            field=models.CharField(choices=[('social', 'Very Social'), ('moderate', 'Moderately Social'), ('private', 'Private Person')], default='moderate', max_length=20),
        ),
    ]
