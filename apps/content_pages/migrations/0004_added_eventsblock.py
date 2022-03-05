# Generated by Django 3.2.12 on 2022-02-28 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0003_remove_event_date'),
        ('content_pages', '0003_alter_orderedimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Блок спектаклей',
                'verbose_name_plural': 'Блоки спектаклей',
            },
        ),
        migrations.CreateModel(
            name='OrderedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок в блоке')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_events', to='content_pages.eventsblock')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_events', to='afisha.event', verbose_name='Событие')),
            ],
            options={
                'verbose_name': 'Содержимое блока',
                'verbose_name_plural': 'Содержимое блоков',
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='performancesblock',
            name='items',
        ),
        migrations.DeleteModel(
            name='OrderedPerformance',
        ),
        migrations.DeleteModel(
            name='PerformancesBlock',
        ),
        migrations.AddField(
            model_name='eventsblock',
            name='items',
            field=models.ManyToManyField(related_name='events_blocks', through='content_pages.OrderedEvent', to='afisha.Event'),
        ),
    ]
