# Generated by Django 4.0 on 2022-03-22 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_order_payment_status_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='order',
            new_name='yourorder',
        ),
    ]
