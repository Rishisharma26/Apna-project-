# Generated by Django 4.0 on 2022-03-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_menu_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='availablity',
            field=models.CharField(default='available', max_length=20),
        ),
        migrations.AddField(
            model_name='menu',
            name='item_desc',
            field=models.CharField(default='enjoy your food', max_length=50),
        ),
        migrations.AddField(
            model_name='menu',
            name='pic',
            field=models.FileField(default='abc.jpg', upload_to='menuimg/'),
        ),
    ]
