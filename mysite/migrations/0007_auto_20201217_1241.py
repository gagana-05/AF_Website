# Generated by Django 2.2.12 on 2020-12-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20201217_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(default=2, upload_to='images/blog'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
    ]