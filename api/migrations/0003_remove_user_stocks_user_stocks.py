# Generated by Django 4.1.7 on 2023-03-27 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_money_current'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='stocks',
        ),
        migrations.AddField(
            model_name='user',
            name='stocks',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.stock'),
            preserve_default=False,
        ),
    ]