# Generated by Django 4.0 on 2022-03-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_mpic_menu_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='pic',
            field=models.FileField(blank=True, default='abc.jpg', null=True, upload_to='menuimg/'),
        ),
    ]
