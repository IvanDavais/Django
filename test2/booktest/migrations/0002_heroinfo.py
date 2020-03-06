# Generated by Django 2.2.5 on 2020-02-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=200)),
                ('isDelete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(on_delete='SET_DEFAULT', to='booktest.BookInfo')),
            ],
        ),
    ]
