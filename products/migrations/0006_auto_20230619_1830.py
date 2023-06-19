# Generated by Django 3.2.18 on 2023-06-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230616_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pre_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Pre sale price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Rating'),
        ),
    ]
