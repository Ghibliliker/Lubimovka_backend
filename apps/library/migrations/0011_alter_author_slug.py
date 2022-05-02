# Generated by Django 3.2.12 on 2022-03-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0010_author_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text="Если не заполнено, будет сформировано автоматически",
                unique=True,
                verbose_name="Транслит фамилии для формирования адресной строки",
            ),
        ),
    ]