# Generated by Django 3.0.8 on 2020-07-29 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=20)),
                ('comment_text', models.CharField(max_length=200)),
                ('comment_data', models.DateTimeField(verbose_name='date posted')),
                ('comment_like', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_main.Post')),
            ],
        ),
    ]