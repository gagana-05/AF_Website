# Generated by Django 3.0.5 on 2020-05-12 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_to_display', models.IntegerField(default=1)),
                ('bg_img', models.ImageField(upload_to='images/event')),
                ('small_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/gallery')),
                ('alt_text', models.CharField(max_length=50)),
                ('display_on_index', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('roll_number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=300)),
                ('insta', models.URLField(default=' ')),
                ('linkdin', models.URLField(default=' ')),
                ('member_img', models.ImageField(upload_to='images/members')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('blog_filter', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='mysite.Member')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]