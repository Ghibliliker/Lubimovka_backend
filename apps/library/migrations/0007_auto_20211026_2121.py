# Generated by Django 3.2.8 on 2021-10-26 21:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_person_image'),
        ('library', '0006_updated_performance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author_plays_links',
        ),
        migrations.RemoveField(
            model_name='author',
            name='other_links',
        ),
        migrations.RemoveField(
            model_name='author',
            name='other_plays_links',
        ),
        migrations.RemoveField(
            model_name='author',
            name='social_network_links',
        ),
        migrations.RemoveField(
            model_name='play',
            name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='plays',
            field=models.ManyToManyField(blank=True, related_name='authors', to='library.Play', verbose_name='Пьесы автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='achievements',
            field=models.ManyToManyField(blank=True, related_name='authors', to='library.Achievement', verbose_name='Достижения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.person', verbose_name='Человек'),
        ),
        migrations.AlterField(
            model_name='otherlink',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_links', to='library.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='otherplay',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_plays_links', to='library.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='play',
            name='url_download',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на скачивание пьесы'),
        ),
        migrations.AlterField(
            model_name='play',
            name='url_reading',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на читку'),
        ),
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2021)], verbose_name='Год написания пьесы'),
        ),
        migrations.AlterField(
            model_name='socialnetworklink',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', to='library.author', verbose_name='Автор'),
        ),
    ]
