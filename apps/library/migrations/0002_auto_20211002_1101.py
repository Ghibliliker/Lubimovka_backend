# Generated by Django 3.2.7 on 2021-10-02 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_person_email'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(help_text='Не более 40 символов', max_length=40, verbose_name='Достижения в виде тега')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='authors_plays_links',
            field=models.ManyToManyField(related_name='author_authorsplayslinks', to='library.Play', verbose_name='Ссылки на пьесы автора'),
        ),
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(default=1, max_length=3000, verbose_name='Текст про автора'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.person', verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='quote',
            field=models.CharField(default=1, max_length=200, verbose_name='Цитата'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OtherPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('link', models.URLField(max_length=1000, verbose_name='Ссылка на скачивание файла')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Другая пьеса',
                'verbose_name_plural': 'Другие пьесы',
            },
        ),
        migrations.CreateModel(
            name='LinkSocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('fb', 'Facebook'), ('inst', 'Instagram'), ('ytube', 'YouTube'), ('tlgrm', 'Telegram'), ('vk', 'Вконтакте')], max_length=200, verbose_name='Название')),
                ('link', models.URLField(max_length=500, verbose_name='Ссылка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Ссылка на социальную сеть',
                'verbose_name_plural': 'Ссылки на социальные сети',
            },
        ),
        migrations.CreateModel(
            name='LinkOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('link', models.URLField(max_length=500, verbose_name='Ссылка')),
                ('anchored', models.BooleanField(help_text='Закрепить запись вверху страницы или нет', verbose_name='Закрепить вверху страницы')),
                ('serial_number', models.PositiveSmallIntegerField(help_text='Указывается для формирования порядка вывода информации', verbose_name='Порядковый номер')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Ссылка на сторонний ресурс',
                'verbose_name_plural': 'Ссылки на стороннии ресурсы',
                'ordering': ['serial_number'],
            },
        ),
        migrations.AddField(
            model_name='author',
            name='achievements',
            field=models.ManyToManyField(to='library.Achievement', verbose_name='Достижения'),
        ),
        migrations.AddField(
            model_name='author',
            name='other_links',
            field=models.ManyToManyField(related_name='author_otherlinks', to='library.LinkOther', verbose_name='Ссылки на внешние ресурсы'),
        ),
        migrations.AddField(
            model_name='author',
            name='other_plays_links',
            field=models.ManyToManyField(blank=True, related_name='author_otherplayslinks', to='library.OtherPlay', verbose_name='Ссылки на другие пьесы'),
        ),
        migrations.AddField(
            model_name='author',
            name='social_network_links',
            field=models.ManyToManyField(related_name='author_socialnetworklinks', to='library.LinkSocialNetwork', verbose_name='Ссылки на социальные сети'),
        ),
    ]
