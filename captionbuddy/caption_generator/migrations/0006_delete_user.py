# Generated by Django 5.0.1 on 2024-01-22 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caption_generator', '0005_user_is_staff_alter_user_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
