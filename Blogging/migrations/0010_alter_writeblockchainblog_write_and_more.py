# Generated by Django 4.1.7 on 2024-04-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogging', '0009_alter_writeblockchainblog_topic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeblockchainblog',
            name='write',
            field=models.TextField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='writeroboticsblog',
            name='write',
            field=models.TextField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='writetechnologyblog',
            name='write',
            field=models.TextField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='writewebblog',
            name='write',
            field=models.TextField(max_length=8000),
        ),
    ]