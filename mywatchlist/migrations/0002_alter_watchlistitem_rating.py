# Generated by Django 4.1 on 2022-11-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
