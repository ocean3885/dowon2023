# Generated by Django 4.1.3 on 2022-12-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0012_remove_submit_first_name_kr"),
    ]

    operations = [
        migrations.AddField(
            model_name="submit",
            name="fav_name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
