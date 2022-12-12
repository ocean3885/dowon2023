from django.db import models
import datetime

class Submit(models.Model):

    class Meta:
        ordering = ['-created']

    CATEGORY_CHOICES = [
        ("jm","신생아작명"),
        ("gm","개명"),
        ("sj","사주상담"),
        ("gh","궁합"),
        ("ti","택일"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parents_name = models.CharField(max_length=25, blank=True)
    first_name_kr = models.CharField(max_length=25, blank=True)
    first_name_ch = models.CharField(max_length=25, blank=True)
    avoid_name = models.CharField(max_length=100, blank=True)
    adress = models.CharField(max_length=100, blank=True)
    phonnumber = models.CharField(max_length=20)
    email = models.EmailField(blank=True,max_length=254)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50,blank=True)
    submit = models.ForeignKey(Submit, on_delete=models.CASCADE, related_name='persons')
    gen = models.CharField(max_length=1)
    sl = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    TIME_CHOICES = [
        ("자","子시 23:30~01:30"), ("축","丑시 01:30~03:30"), ("인","寅시 03:30~05:30"), ("묘","卯시 05:30~07:30"),
        ("진","辰시 07:30~09:30"), ("사","巳시 09:30~11:30"), ("오","午시 11:30~13:30"), ("미","未시 13:30~15:30"),
        ("신","申시 15:30~17:30"), ("유","酉시 17:30~19:30"), ("술","戌시 19:30~21:30"), ("해","亥시 21:30~23:30"),
    ]
    time = models.CharField(max_length=1, choices=TIME_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

