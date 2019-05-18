# Generated by Django 2.2.1 on 2019-05-17 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('order_no', models.CharField(help_text='enter the order number', max_length=128, primary_key=True, serialize=False)),
                ('title', models.TextField(default='', help_text='enter the title', max_length=128)),
                ('dt_created', models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 17, 9, 25, 34, 474527, tzinfo=utc))),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('assig', 'yes'), ('not_assig', 'free')], default='NOT_ASSIGN', help_text='deliverd or not delivered', max_length=128)),
                ('priority', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('medium', 'medium')], default='MEDIUM_PRIORITY', help_text='priority can be high/low/medium', max_length=128)),
                ('task', models.CharField(choices=[('accepts', 'accepts'), ('not_accepts', 'not_accepts')], default='TASK_NOT_ASSIGN', help_text='Accepts or not', max_length=128)),
            ],
        ),
    ]
