# Generated by Django 4.2.5 on 2023-09-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapi_app', '0003_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='flag',
            field=models.BooleanField(default=True),
        ),
    ]