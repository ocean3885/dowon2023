# Generated by Django 4.1.3 on 2022-12-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msr_database", "0002_alter_calendadata_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendadata", name="cd_ld", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="calendadata", name="cd_lm", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="calendadata", name="cd_sd", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="calendadata", name="cd_sm", field=models.IntegerField(),
        ),
    ]
