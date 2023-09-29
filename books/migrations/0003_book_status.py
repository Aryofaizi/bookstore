# Generated by Django 4.2.1 on 2023-06-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('pub', 'published'), ('drf', 'draft')], default='pub', max_length=3),
            preserve_default=False,
        ),
    ]