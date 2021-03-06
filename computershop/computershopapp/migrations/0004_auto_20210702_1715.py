# Generated by Django 3.2.5 on 2021-07-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computershopapp', '0003_rename_registers_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='img',
        ),
        migrations.AddField(
            model_name='task',
            name='email',
            field=models.EmailField(default='default', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='first_name',
            field=models.TextField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='last_name',
            field=models.TextField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='password',
            field=models.TextField(),
        ),
    ]
