# Generated by Django 3.2 on 2021-07-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210707_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Payment',
            field=models.BooleanField(default=True),
        ),
    ]
