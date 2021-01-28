from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


class Subjects(models.Model):
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name_plural = "subjects"


class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='upload/', default='upload/default.png')
    email  = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    subjects_taken = models.ManyToManyField(Subjects)


    def clean_subjects(self):
        subjects = self.cleaned_data['subjects_taken']
        if len(subjects) > 3:
            raise forms.ValidationError('You can add maximum 3 subjects')
        return subjects

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Teachers"




