# Generated by Django 5.0.1 on 2024-02-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caption_generator', '0010_remove_image_imagefilenname_alter_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caption',
            name='captionId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
