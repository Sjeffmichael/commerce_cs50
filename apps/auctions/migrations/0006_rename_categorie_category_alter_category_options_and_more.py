# Generated by Django 4.0.3 on 2022-03-28 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_listing_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='categorie',
            new_name='category',
        ),
    ]