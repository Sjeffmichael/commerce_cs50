# Generated by Django 4.0.3 on 2022-03-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_user_alter_listing_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_image',
            field=models.ImageField(blank=True, null=True, upload_to='auctions/', verbose_name='Image Listing'),
        ),
    ]
