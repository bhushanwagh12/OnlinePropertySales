# Generated by Django 2.1.4 on 2019-02-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190201_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmodel',
            name='dateofsale',
            field=models.CharField(max_length=40),
        ),
    ]
