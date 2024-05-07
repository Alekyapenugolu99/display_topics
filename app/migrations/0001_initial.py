# Generated by Django 5.0.3 on 2024-04-24 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100, unique=True)),
                ('dloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('Grade', models.IntegerField(primary_key=True, serialize=False)),
                ('losal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('highsal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('Sal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Comm', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Hiredate', models.DateField()),
                ('Deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('Mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]
