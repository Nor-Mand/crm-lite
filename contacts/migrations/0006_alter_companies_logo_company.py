# Generated by Django 4.1.3 on 2022-11-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0005_alter_companies_logo_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companies",
            name="logo_company",
            field=models.ImageField(
                blank=True, default="", upload_to="profile_pictures/"
            ),
        ),
    ]
