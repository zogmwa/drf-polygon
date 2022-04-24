from django.db import migrations, models
from apps.polygons.constants import POLYGONS_3_20


def fwd(apps, schema_editor):
    Polygon = apps.get_model('polygons', 'Polygon')
    polygons = [
        Polygon(
            name=POLYGONS_3_20[index]['name'], 
            num_sides=POLYGONS_3_20[index]['num_sides']
        ) 
        for index in range(len(POLYGONS_3_20))
    ]
    Polygon.objects.bulk_create(polygons)


def rev():
    pass


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('num_sides', models.PositiveIntegerField()),
            ],
        ),
        migrations.RunPython(fwd, rev)
    ]
