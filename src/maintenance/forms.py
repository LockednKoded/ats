from django import forms
from .models import Worker


class SearchForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = [
            'worker_type',
        ]


class UserForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = [
            'user',
        ]


class AssignForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = [
            'user',
            'worker_type'
        ]
