# Generated by Django 4.0.6 on 2022-07-20 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_weight', '0002_remove_plan_numbertrainingperweek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
