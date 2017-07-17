from django import forms
from .models import VehicleDetail, ParkingSpot


class ParkingForm(forms.ModelForm):

    class Meta:
        model = ParkingSpot
        fields = [
            'spots_occupied',
            'spots_available',
        ]


class VehicleForm(forms.ModelForm):

    class Meta:
        model = VehicleDetail
        fields = [
            'vehicle_no',
            'vehicle_type',
            'date',
            'time_in',
            'time_out',
        ]

        def clean__vehicle_no(self):
            vehicle_no = self.cleaned_data.get('vehicle_no')

            vehicle_qs = VehicleDetail.objects.get(vehicle_no=vehicle_no)
            if vehicle_qs.exists():
                raise forms.ValidationError("Vehicle with same No. already exists")
