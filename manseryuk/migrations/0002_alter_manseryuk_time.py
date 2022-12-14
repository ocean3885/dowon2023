# Generated by Django 4.1.3 on 2022-11-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manseryuk", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manseryuk",
            name="time",
            field=models.CharField(
                choices=[
                    ("자", "23:30~01:30"),
                    ("축", "01:30~03:30"),
                    ("인", "03:30~05:30"),
                    ("묘", "05:30~07:30"),
                    ("진", "07:30~09:30"),
                    ("사", "09:30~11:30"),
                    ("오", "11:30~13:30"),
                    ("미", "13:30~15:30"),
                    ("신", "15:30~17:30"),
                    ("유", "17:30~19:30"),
                    ("술", "19:30~21:30"),
                    ("해", "21:30~23:30"),
                ],
                max_length=1,
            ),
        ),
    ]
