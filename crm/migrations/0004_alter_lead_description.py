# Generated by Django 4.1.3 on 2022-11-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_lead_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="Description"),
        ),
    ]
