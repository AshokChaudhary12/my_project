# Generated by Django 4.2.11 on 2024-05-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventories',
            name='purchase_date',
            field=models.DateField(),
        ),
    ]
