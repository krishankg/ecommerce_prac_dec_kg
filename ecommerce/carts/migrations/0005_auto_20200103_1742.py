# Generated by Django 3.0 on 2020-01-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20200103_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='subtotal',
        ),
        migrations.AddField(
            model_name='cart',
            name='total_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]