from django import forms
from .models import Teachers
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


class TeachersModelForm(forms.ModelForm):

    # def clean(self):
    #     subjects = self.cleaned_data['subjects_taken']
    #     if len(subjects) > 3:
    #         raise forms.ValidationError('You can add maximum 3 subjects')
    #     return subjects

    # def regions_changed(sender, **kwargs):
    #     if kwargs['instance'].regions.count() > 3:
    #         raise ValidationError("You can't assign more than three regions")

    def clean(self):
        subjects = self.cleaned_data.get('subjects_taken')
        if subjects and subjects.count() > 5:
            raise ValidationError('Maximum three subjects are allowed.')

        return self.cleaned_data

    class Meta:
        model = Teachers
        fields = ('first_name','last_name',
        'profile_picture','email','phone_number','room_number','subjects_taken')
