# Generated by Django 4.1.3 on 2022-12-06 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_alter_submit_options_remove_submit_day_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="submit",
            name="adress",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="submit",
            name="avoid_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="submit",
            name="first_name_ch",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name="submit",
            name="first_name_kr",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name="submit",
            name="parents_name",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name="submit",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
