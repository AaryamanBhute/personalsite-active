# Generated by Django 3.2.7 on 2022-04-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]