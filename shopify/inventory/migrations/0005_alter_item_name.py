# Generated by Django 4.0.4 on 2022-05-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_item_deleted_alter_item_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
