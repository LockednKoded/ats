from django import forms

from .models import Flight, Crew


class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight
        fields = [
            'flight_no',
            'airline',
            'origin',
            'destination',
            'terminal',
            'concourse',
            'fare',
            'total_seats',
            'booked_seats',
            'approved_plan',
            'operation_days',
            'scheduled_arrival',
            'scheduled_departure',
            'revised_arrival',
            'revised_departure',
        ]

        def clean(self):
            scheduled_arrival = self.cleaned_data.get('scheduled_arrival')
            scheduled_departure = self.cleaned_data.get('scheduled_departure')
            revised_arrival = self.cleaned_data.get('revised_arrival')
            revised_departure = self.cleaned_data.get('revised_departure')

            if revised_arrival < scheduled_arrival:
                raise forms.ValidationError('Scheduled arrival should be before revised arrival')
            if revised_departure < scheduled_departure:
                raise forms.ValidationError('Scheduled departure should be before revised departure')
            return super(FlightForm, self).clean()

        def clean__flight_no(self):
            flight_no = self.cleaned_data.get('flight_no')

            flights_qs = Flight.objects.get(flight_no=flight_no)
            if flights_qs.exists():
                raise forms.ValidationError("Flight with same no. already exists")


class CrewForm(forms.ModelForm):

    class Meta:
        model = Crew
        fields = [
            'crew_id',
            'name',
            'pilot',
            'experience',
            'license_no',
            'ph_no',
            'photo',
            'in_service',
            'flights',
        ]

        def clean__crew_id(self):
            crew_id = self.cleaned_data.get('crew_id')

            crew_qs = Crew.objects.get(crew_id=crew_id)
            if crew_qs.exists():
                raise forms.ValidationError("Crew with same id already exists")