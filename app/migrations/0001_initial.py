# Generated by Django 2.2.4 on 2019-08-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_name', models.CharField(max_length=20)),
                ('blog_body', models.TextField()),
                ('blog_time', models.DateTimeField()),
                ('blog_viewnumber', models.IntegerField(db_column='blog_viewNumber')),
                ('blog_likenumber', models.IntegerField(db_column='blog_likeNumber')),
                ('blog_state', models.IntegerField()),
            ],
            options={
                'db_table': 'blog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField(unique=True)),
                ('tag_id', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'blog_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_time', models.DateTimeField()),
                ('review_body', models.TextField()),
                ('return_user', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('user_password', models.CharField(max_length=20)),
                ('user_mail', models.CharField(max_length=255, unique=True)),
                ('user_state', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
