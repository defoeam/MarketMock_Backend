# Generated by Django 4.1.7 on 2023-04-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_stock_shares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstocks',
            name='shares',
        ),
        migrations.AddField(
            model_name='stock',
            name='shares',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]