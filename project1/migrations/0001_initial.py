# Generated by Django 5.1 on 2024-11-07 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HANGHOA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ten', models.CharField(max_length=200)),
                ('MoTa', models.TextField(blank=True)),
                ('DonViTinh', models.CharField(choices=[('Kg', 'Kilogram'), ('Cai', 'Cái'), ('Chai', 'Chai'), ('Hop', 'Hộp')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='KHO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ten', models.CharField(max_length=100)),
                ('DiaChi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KHOHANGHOA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoLuong', models.IntegerField()),
                ('HangHoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.hanghoa')),
                ('Kho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.kho')),
            ],
        ),
        migrations.AddField(
            model_name='hanghoa',
            name='Kho',
            field=models.ManyToManyField(through='project1.KHOHANGHOA', to='project1.kho'),
        ),
    ]