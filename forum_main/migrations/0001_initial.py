from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=20)),
                ('post_text', models.CharField(max_length=200)),
                ('post_data', models.DateTimeField(verbose_name='date posted')),
                ('post_like', models.IntegerField(default=0)),
            ],
        ),
    ]
