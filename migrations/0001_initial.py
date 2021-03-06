# Generated by Django 2.1.4 on 2019-01-04 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import formula_one.utils.upload_to
import formula_one.validators.aspect_ratio
import formula_one.validators.year_relation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_PERSON_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('acronym', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=127)),
                ('slug', models.SlugField(max_length=127, unique=True)),
                ('year_of_inception', models.IntegerField(blank=True, null=True, validators=[formula_one.validators.year_relation.YearRelationValidator('<=')])),
                ('short_description', models.CharField(blank=True, max_length=127)),
                ('about', models.TextField()),
                ('mission', models.TextField()),
                ('logo', models.ImageField(blank=True, max_length=255, null=True, upload_to=formula_one.utils.upload_to.UploadTo('groups', 'logos'), validators=[formula_one.validators.aspect_ratio.AspectRatioValidator(1)])),
                ('cover_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=formula_one.utils.upload_to.UploadTo('groups', 'cover_images'))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=127)),
                ('post', models.CharField(blank=True, max_length=127)),
                ('has_edit_rights', models.BooleanField(default=False)),
                ('has_admin_rights', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_PERSON_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=formula_one.utils.upload_to.UploadTo('groups', 'post_images'))),
                ('text', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, through='groups.Membership', to=settings.KERNEL_PERSON_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('person', 'group')},
        ),
    ]
