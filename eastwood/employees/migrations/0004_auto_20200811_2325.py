# Generated by Django 3.1 on 2020-08-11 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20200811_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='ended_work',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='started_work',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
        ),
    ]
