# Generated by Django 4.2.1 on 2023-10-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.CharField(default=1, max_length=150, verbose_name='создан в'),
            preserve_default=False,
        ),
    ]
