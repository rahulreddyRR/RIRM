# Generated by Django 3.0.4 on 2020-03-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='Client_Value',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]