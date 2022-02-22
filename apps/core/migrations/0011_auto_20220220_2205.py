# Generated by Django 3.2.12 on 2022-02-20 19:05

from django.db import migrations, models


def set_status(apps, schema_editor):
    Status = apps.get_model("core", "Status")
    Status.objects.create(
        name="В работе",
        next_button_name="Отправить на проверку",
        ordering=1,
    )
    Status.objects.create(
        name="На проверке",
        previous_button_name="Вернуть в работу",
        next_button_name="Подготовить для публикации",
        ordering=2,
    )
    Status.objects.create(
        name="Готово к публикации",
        previous_button_name="Вернуть на проверку",
        next_button_name="Опубликовать",
        ordering=3,
    )
    Status.objects.create(
        name="Опубликовано",
        previous_button_name="Подготовить для публикации",
        next_button_name="Снять с публикации",
        ordering=4,
        protected=True,
    )
    Status.objects.create(
        name="Снято с публикации",
        previous_button_name="Опубликовать заново",
        ordering=5,
        protected=True,
    )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_setting_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('previous_button_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Название кнопки возврата в предыдущее состояние')),
                ('next_button_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Название кнопки перехода в следующее состояние')),
                ('protected', models.BooleanField(default=False, verbose_name='Требуются особые права для установки данного статуса')),
                ('ordering', models.PositiveSmallIntegerField(blank=True, unique=True, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Статус страницы',
                'verbose_name_plural': 'Статусы страницы',
                'ordering': ('ordering',),
            },
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='Загрузите фотографию', upload_to='images/core/', verbose_name='Изображение'),
        ),
        migrations.RunPython(
            set_status,
        )
    ]