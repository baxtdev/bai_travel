# Generated by Django 5.0.1 on 2024-02-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_remove_tours_photo_tours_discount_alter_zayavka_tour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phototours',
            name='photo',
            field=models.ImageField(upload_to='uploads/images/'),
        ),
    ]
