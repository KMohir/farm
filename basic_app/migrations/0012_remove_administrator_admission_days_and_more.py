# Generated by Django 4.2.7 on 2024-12-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0011_banner_author_post_en_banner_author_post_ru_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="administrator",
            name="admission_days",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="admission_days_en",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="admission_days_ru",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="admission_days_uz",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="email",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="f_name",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="f_name_en",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="f_name_ru",
        ),
        migrations.RemoveField(
            model_name="administrator",
            name="f_name_uz",
        ),
        migrations.AddField(
            model_name="administrator",
            name="name",
            field=models.CharField(
                default=1, max_length=255, verbose_name="To'liq ismi"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="administrator",
            name="name_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="To'liq ismi"
            ),
        ),
        migrations.AddField(
            model_name="administrator",
            name="name_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="To'liq ismi"
            ),
        ),
        migrations.AddField(
            model_name="administrator",
            name="name_uz",
            field=models.CharField(
                max_length=255, null=True, verbose_name="To'liq ismi"
            ),
        ),
        migrations.AddField(
            model_name="administrator",
            name="title",
            field=models.CharField(default=1, max_length=255, verbose_name="Lavozimi"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="administrator",
            name="position",
            field=models.CharField(max_length=255, verbose_name="Lavozimi"),
        ),
        migrations.AlterField(
            model_name="administrator",
            name="position_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AlterField(
            model_name="administrator",
            name="position_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AlterField(
            model_name="administrator",
            name="position_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
    ]
