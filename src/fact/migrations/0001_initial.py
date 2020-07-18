# Generated by Django 2.2 on 2020-07-18 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_image', models.ImageField(upload_to='achivement/')),
                ('about_image', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=500)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calculate_BMI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(max_length=10)),
                ('weight', models.FloatField(max_length=10)),
                ('age', models.FloatField(max_length=10)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('user_id', models.ImageField(blank=True, default='', null=True, upload_to='staff/')),
                ('pic', models.ImageField(null=True, upload_to='client/')),
                ('join_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_image', models.ImageField(upload_to='equipment/')),
            ],
        ),
        migrations.CreateModel(
            name='Home_pic_moti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_image', models.ImageField(upload_to='home/')),
                ('motivation', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('three', '3'), ('six', '6'), ('twelve', '12')], default='six', max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('user_id', models.ImageField(blank=True, default='', null=True, upload_to='staff/')),
                ('pic', models.ImageField(null=True, upload_to='staff/')),
                ('join_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('text', models.TextField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('star', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualification', models.TextField(max_length=200)),
                ('trainer_id', models.ImageField(blank=True, default='', null=True, upload_to='trainer/')),
                ('facebook', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('tweet', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('picture', models.ImageField(blank=True, default='', null=True, upload_to='trainer/')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
            ],
        ),
    ]