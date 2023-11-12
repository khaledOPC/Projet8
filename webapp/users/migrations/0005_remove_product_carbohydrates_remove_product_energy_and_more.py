# Generated by Django 4.2 on 2023-09-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_product_carbohydrates_product_energy_product_fat_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="carbohydrates",
        ),
        migrations.RemoveField(
            model_name="product",
            name="energy",
        ),
        migrations.RemoveField(
            model_name="product",
            name="fat",
        ),
        migrations.RemoveField(
            model_name="product",
            name="fibers",
        ),
        migrations.RemoveField(
            model_name="product",
            name="proteins",
        ),
        migrations.RemoveField(
            model_name="product",
            name="salt",
        ),
        migrations.RemoveField(
            model_name="product",
            name="saturated_fat",
        ),
        migrations.RemoveField(
            model_name="product",
            name="sugars",
        ),
        migrations.AddField(
            model_name="product",
            name="nutrition_data",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
