# Generated by Django 3.0.2 on 2020-01-26 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('available', models.BooleanField()),
                ('color', models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], default='RED', max_length=120)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Authors')),
            ],
        ),
    ]
