# Generated by Django 3.2 on 2021-07-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_contact_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='Contact',
            field=models.CharField(max_length=11),
        ),
    ]
