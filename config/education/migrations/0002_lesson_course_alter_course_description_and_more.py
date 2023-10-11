# Generated by Django 4.2.6 on 2023-10-11 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='курс'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='education/', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название'),
        ),
    ]
