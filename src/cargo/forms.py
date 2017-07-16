from django import forms

from .models import cargo


class CargoForm(forms.ModelForm):

    class Meta:
        model = cargo
        fields = [
            'cargo_no',
            'cargo_airline',
            'original',
            'destination',
            'terminal',
            'weight',
            #'fare',
           #'scheduled_arrival',
           'scheduled_departure',
            #'revised_arrival',
           # 'revised_departure',
        ]

        def clean__cargo_no(self):
            cargo_no = self.cleaned_data.get('cargo.cargo_no')

            cargo_qs = cargo.objects.get(cargo_no=cargo.cargo_no)
            if cargo_qs.exists():
                raise forms.ValidationError("Cargo Shipment with same no. already exists")


