# Generated by Django 4.0.8 on 2023-03-05 22:55

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orders_order_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_UUID',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', auto_created=True, editable=False, length=10, max_length=10, prefix='', unique=True, verbose_name='UUID заказа'),
        ),
    ]
