# Generated by Django 4.2.1 on 2023-06-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]
