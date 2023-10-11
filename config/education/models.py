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
    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               related_name='course', verbose_name='курс',
                               **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    CASH = "Наличные"
    CARD = "Безналичные"

    PAYMENT_CHOICES = [
        (CASH, "Наличные"),
        (CARD, "Безналичные"),
    ]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             verbose_name='пользователь')
    date_of_payment = models.DateField(verbose_name='дата платежа')
    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               verbose_name='оплаченный курс')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE,
                               verbose_name='оплаченный урок')
    sum_of_payment = models.IntegerField(verbose_name='сумма платежа')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES,
                                      verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.date_of_payment} - {self.sum_of_payment}'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
