# Generated by Django 4.2.7 on 2024-11-08 09:50

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='admission_days_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Qabul kunlari'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='admission_days_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Qabul kunlari'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='admission_days_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Qabul kunlari'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='f_name_en',
            field=models.CharField(max_length=100, null=True, verbose_name="To'liq ismi"),
        ),
        migrations.AddField(
            model_name='administrator',
            name='f_name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name="To'liq ismi"),
        ),
        migrations.AddField(
            model_name='administrator',
            name='f_name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name="To'liq ismi"),
        ),
        migrations.AddField(
            model_name='administrator',
            name='position_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Lavozimi'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='position_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Lavozimi'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='position_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Lavozimi'),
        ),
        migrations.AddField(
            model_name='interactivemap',
            name='region_name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Viloyat nomi'),
        ),
        migrations.AddField(
            model_name='interactivemap',
            name='region_name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Viloyat nomi'),
        ),
        migrations.AddField(
            model_name='interactivemap',
            name='region_name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Viloyat nomi'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='news',
            name='author_post_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Muallifi'),
        ),
        migrations.AddField(
            model_name='news',
            name='author_post_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Muallifi'),
        ),
        migrations.AddField(
            model_name='news',
            name='author_post_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='Muallifi'),
        ),
        migrations.AddField(
            model_name='news',
            name='post_en',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name="To'liq mazmuni"),
        ),
        migrations.AddField(
            model_name='news',
            name='post_ru',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name="To'liq mazmuni"),
        ),
        migrations.AddField(
            model_name='news',
            name='post_uz',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name="To'liq mazmuni"),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='posts',
            name='author_post_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Muallifi'),
        ),
        migrations.AddField(
            model_name='posts',
            name='author_post_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Muallifi'),
        ),
        migrations.AddField(
            model_name='posts',
            name='author_post_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='Muallifi'),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_en',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name="To'liq mazmuni"),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_ru',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name="To'liq mazmuni"),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_uz',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name="To'liq mazmuni"),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
    ]