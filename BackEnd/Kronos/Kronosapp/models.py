from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class DocumentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Nationality(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class ContactInformation(models.Model):
    postalCode = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    streetNumber = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)


class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='logos/')
    email = models.EmailField(max_length=255, unique=True)
    contactInfo = models.OneToOneField(ContactInformation, on_delete=models.SET_NULL)
    directives = models.ManyToManyField('CustomUser')


class CustomUser(AbstractUser):
    GENDER_CHOICES = {
        'male': 'Masculino',
        'female': 'Femenino'
    }
    firstName = models.CharField(max_length=255,blank=True, null=True)
    lastName = models.CharField(max_length=255,blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES,blank=True, null=True)
    email = models.CharField(max_length=255,blank=True, null=False, unique=True)
    document = models.CharField(max_length=255,blank=True, null=True)
    hoursToWork = models.IntegerField(blank=True, null=True)
    documentType = models.ForeignKey(DocumentType, on_delete=models.SET_NULL,blank=True, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL,blank=True, null=True)
    contactInfo = models.OneToOneField(ContactInformation, on_delete=models.SET_NULL,blank=True, null=True)
    email_verified = models.BooleanField(default=False,blank=True, null=True)
    verification_token = models.UUIDField(default=uuid.uuid4,blank=True, null=True)

    def is_directive(self, school: School):
        return self in school.directives.all()


class Module(models.Model):
    moduleNumber = models.IntegerField()
    dayId = models.CharField(max_length=10, choices=[
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ])
    endTime = models.TimeField()
    startTime = models.TimeField()
    schoolId = models.ForeignKey('Schools', on_delete=models.CASCADE)


class AvailabilityState(models.Model):
    name = models.CharField(max_length=255)
    isEnabled = models.BooleanField()


class TeacherAvailability(models.Model):
    moduleId = models.ForeignKey('Modules', on_delete=models.CASCADE)
    teacherId = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    loadDate = models.DateTimeField()
    availabilityStateId = models.ForeignKey('AvailabilityState', on_delete=models.CASCADE)


class Year(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    number = models.CharField(max_length=255)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    yearId = models.ForeignKey('Years', on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=255)
    studyPlan = models.TextField()
    description = models.CharField(max_length=255)
    weeklyHours = models.IntegerField()
    color = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    yearId = models.ForeignKey('Years', on_delete=models.CASCADE)
    courseId = models.ForeignKey('Courses', on_delete=models.SET_NULL)


class TeacherSubjectSchool(models.Model):
    schoolId = models.ForeignKey('Schools', on_delete=models.CASCADE)
    subjectId = models.ForeignKey('Subjects', on_delete=models.CASCADE)
    teacherId = models.ForeignKey('CustomUser', on_delete=models.CASCADE)


class Action(models.Model):
    name = models.CharField(max_length=255)
    isEnabled = models.BooleanField()


class Schedules(models.Model):
    date = models.DateTimeField()
    actionId = models.ForeignKey('Actions', on_delete=models.SET_NULL)
    moduleId = models.ForeignKey('Modules', on_delete=models.CASCADE)
    tssId = models.ForeignKey('TeacherSubjectSchool', on_delete=models.CASCADE)


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    eventType = models.ForeignKey(EventType, on_delete=models.SET_NULL)
    affiliated_teachers = models.ManyToManyField(CustomUser)