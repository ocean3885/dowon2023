# Generated by Django 4.1.3 on 2022-12-12 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_alter_person_gen_alter_person_sl_alter_person_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="submit", name="first_name_kr",),
    ]
