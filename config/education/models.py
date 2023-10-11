from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, **NULLABLE,
                             verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    picture = models.ImageField(upload_to='new_app/', verbose_name='превью',
                                **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, **NULLABLE,
                             verbose_name='название')
    description = models.CharField(max_length=100, **NULLABLE,
                                   verbose_name='описание')
    picture = models.ImageField(upload_to='education/', **NULLABLE,
                                verbose_name='превью')
    link = models.URLField(max_length=200, **NULLABLE, verbose_name='ссылка')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
