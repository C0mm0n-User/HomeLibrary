from django.db import models


class Book(models.Model):
    title = models.CharField('Название', max_length=32)
    author = models.CharField('Автор', max_length=32)
    cupboard_number = models.CharField('Шкаф', max_length=10)
    shelf_number = models.CharField('Полка', max_length=10)
    comment = models.CharField('Комментарий', max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
