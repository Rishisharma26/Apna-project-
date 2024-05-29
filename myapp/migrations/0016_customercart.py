# Generated by Django 4.0 on 2022-03-16 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_delete_customercart'),
    ]

    operations = [
        migrations.CreateModel(
            name='customercart',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tbooking')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.menu')),
            ],
        ),
    ]
