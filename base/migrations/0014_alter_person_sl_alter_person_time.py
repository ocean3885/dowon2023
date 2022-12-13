# Generated by Django 4.1.3 on 2022-12-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0013_submit_fav_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person", name="sl", field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="person",
            name="time",
            field=models.CharField(
                choices=[
                    ("子시 23:30~01:30", "子시 23:30~01:30"),
                    ("丑시 01:30~03:30", "丑시 01:30~03:30"),
                    ("寅시 03:30~05:30", "寅시 03:30~05:30"),
                    ("卯시 05:30~07:30", "卯시 05:30~07:30"),
                    ("辰시 07:30~09:30", "辰시 07:30~09:30"),
                    ("巳시 09:30~11:30", "巳시 09:30~11:30"),
                    ("午시 11:30~13:30", "午시 11:30~13:30"),
                    ("未시 13:30~15:30", "未시 13:30~15:30"),
                    ("申시 15:30~17:30", "申시 15:30~17:30"),
                    ("酉시 17:30~19:30", "酉시 17:30~19:30"),
                    ("戌시 19:30~21:30", "戌시 19:30~21:30"),
                    ("亥시 21:30~23:30", "亥시 21:30~23:30"),
                ],
                max_length=25,
            ),
        ),
    ]
