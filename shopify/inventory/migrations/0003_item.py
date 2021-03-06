# Generated by Django 4.0.4 on 2022-05-18 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_inventory_location_remove_inventory_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('in_stock', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('deletion_comment', models.CharField(max_length=100)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
    ]
