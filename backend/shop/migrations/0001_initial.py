# Generated by Django 4.0.8 on 2023-03-03 15:27

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование категории')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления категории')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления категории')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MainPageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main_page_slider', verbose_name='Изображение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления изображения')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления изображения')),
            ],
            options={
                'verbose_name': 'изображение в слайдере',
                'verbose_name_plural': 'Изображения в слайдере',
            },
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование подкатегории')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления подкатегории')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления подкатегории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'подкатегорию',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')),
                ('promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена товара со скидкой')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Изображение товара')),
                ('information', models.TextField(blank=True, max_length=100, null=True, verbose_name='Краткая информация о товаре')),
                ('full_information', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Полная информация о товаре')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Остаток товара')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие товара')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategories', verbose_name='Подкатегория товара')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
            },
        ),
    ]
