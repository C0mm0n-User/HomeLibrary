# Generated by Django 3.1.1 on 2020-10-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('author', models.CharField(max_length=20, verbose_name='Автор')),
                ('cupboard_number', models.CharField(max_length=10, verbose_name='Шкаф')),
                ('shelf_number', models.CharField(max_length=10, verbose_name='Полка')),
                ('comment', models.CharField(max_length=50, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]