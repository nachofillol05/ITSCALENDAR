# Generated by Django 5.1 on 2024-09-04 15:16

import Kronosapp.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isEnabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AvailabilityState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isEnabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalCode', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=255)),
                ('streetNumber', models.CharField(max_length=10, validators=[Kronosapp.models.validate_numeric])),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=10)),
                ('logo', models.BinaryField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('contactInfo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.contactinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleNumber', models.IntegerField()),
                ('day', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')], max_length=10)),
                ('endTime', models.TimeField()),
                ('startTime', models.TimeField()),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.school')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=7)),
                ('abbreviation', models.CharField(blank=True, max_length=10)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.school')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studyPlan', models.TextField()),
                ('weeklyHours', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.course')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubjectSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursesubjects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.coursesubjects')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.school')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.action')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.module')),
                ('tssId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.teachersubjectschool')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('number', models.CharField(max_length=1)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='years', to='Kronosapp.school')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.year'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('document', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_picture', models.BinaryField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=10, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('hoursToWork', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=25, null=True, validators=[Kronosapp.models.validate_numeric])),
                ('email_verified', models.BooleanField(default=False)),
                ('verification_token', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True)),
                ('dark_mode', models.BooleanField(default=False)),
                ('color', models.SmallIntegerField(blank=True, null=True)),
                ('contactInfo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.contactinformation')),
                ('documentType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.documenttype')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.nationality')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='year',
            name='preceptors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teachersubjectschool',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TeacherAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loadDate', models.DateTimeField(auto_now_add=True)),
                ('availabilityState', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.availabilitystate')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.module')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='directives',
            field=models.ManyToManyField(blank=True, related_name='directed_schools', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('eventType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Kronosapp.eventtype')),
                ('roles', models.ManyToManyField(to='Kronosapp.role')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kronosapp.school')),
                ('affiliated_teachers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
