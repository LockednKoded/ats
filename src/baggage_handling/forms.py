from django import forms

from .models import BaggageHandling


class BaggageForm(forms.ModelForm):

    class Meta:
        model = BaggageHandling
        fields = [
            'pnr_no',
            'quantity',
            'weight',
            'conveyor_no',
        ]
