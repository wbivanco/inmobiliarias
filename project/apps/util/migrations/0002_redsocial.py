# Generated by Django 3.1.1 on 2020-09-30 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram')], default='facebook', max_length=9)),
                ('url', models.URLField()),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
    ]
