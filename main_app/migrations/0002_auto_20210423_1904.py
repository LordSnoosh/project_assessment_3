# Generated by Django 3.1.7 on 2021-04-23 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wish',
            new_name='WishList',
        ),
    ]
