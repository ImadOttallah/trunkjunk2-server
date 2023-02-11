# Generated by Django 4.1.6 on 2023-02-10 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bandana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('origin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BandanaColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BandanaCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BandanaMarking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BandanaPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.user')),
            ],
        ),
        migrations.CreateModel(
            name='BandanaCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.bandana')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.collection')),
            ],
        ),
        migrations.AddField(
            model_name='bandana',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.bandanacolor'),
        ),
        migrations.AddField(
            model_name='bandana',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.bandanacondition'),
        ),
        migrations.AddField(
            model_name='bandana',
            name='marking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.bandanamarking'),
        ),
        migrations.AddField(
            model_name='bandana',
            name='pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.bandanapattern'),
        ),
        migrations.AddField(
            model_name='bandana',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trunkjunk2api.user'),
        ),
    ]
