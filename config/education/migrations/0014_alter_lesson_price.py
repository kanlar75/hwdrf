# Generated by Django 4.2.6 on 2023-10-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0013_alter_payment_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]
