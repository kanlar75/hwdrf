# Generated by Django 4.2.6 on 2023-10-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_alter_lesson_options_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активна'),
        ),
    ]
