# Generated by Django 2.1.2 on 2018-11-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadPage', '0005_auto_20181030_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.CharField(default=76131, max_length=5),
        ),
    ]
