# Generated by Django 4.1.2 on 2022-10-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='SLug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
