# Generated by Django 3.2.12 on 2022-02-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_settings_change_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='Загрузите фотографию', upload_to='images/core/', verbose_name='Изображение'),
        ),
    ]