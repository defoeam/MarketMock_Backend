# Generated by Django 4.1.7 on 2023-03-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stockId', models.AutoField(primary_key=True, serialize=False)),
                ('StockTicker', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('stocks', models.ManyToManyField(to='api.stock')),
            ],
        ),
    ]