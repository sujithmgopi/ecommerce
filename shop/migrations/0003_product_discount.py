# Generated by Django 2.1.4 on 2019-09-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190904_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Discount',
            field=models.IntegerField(default=0),
        ),
    ]