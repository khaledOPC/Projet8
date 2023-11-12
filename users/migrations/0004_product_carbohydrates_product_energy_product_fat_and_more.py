# Generated by Django 4.2 on 2023-09-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_product_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="carbohydrates",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Glucides (g)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="energy",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Energie (kcal)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="fat",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Matières grasses (g)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="fibers",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Fibres alimentaires (g)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="nutrition_reference",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="proteins",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Protéines (g)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="salt",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Sel (g)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="saturated_fat",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Dont acides gras saturés (g)",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="sugars",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Dont sucres (g)",
            ),
        ),
    ]
