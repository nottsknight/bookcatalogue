# Generated by Django 3.2.6 on 2021-08-13 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('middle_names', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classmark',
            fields=[
                ('number', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(blank=True, max_length=128, null=True)),
                ('author1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author1_set', to='books.author')),
                ('author2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author2_set', to='books.author')),
                ('author3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author3_set', to='books.author')),
                ('author4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author4_set', to='books.author')),
                ('author5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author5_set', to='books.author')),
                ('classmark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.classmark')),
            ],
        ),
    ]
