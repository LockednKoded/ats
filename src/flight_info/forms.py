from django import forms

from .models import Flight, Crew, Airline


class FlightForm(forms.ModelForm):

    DAY_LIST = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )

    days_operational = forms.MultipleChoiceField(choices=DAY_LIST, widget=forms.CheckboxSelectMultiple)
    flight_no = forms.IntegerField(help_text="Enter a unique flight no", label="Flight No")
    approved_plan = forms.BooleanField(help_text="Check if plan is approved", label="Plan approved", required=False)

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

        # def clean__revised_arrival(self):
        #     scheduled_arrival = self.cleaned_data.get('scheduled_arrival')
        #     revised_arrival = self.cleaned_data.get('revised_arrival')
        #
        #     if revised_arrival < scheduled_arrival:
        #         raise forms.ValidationError('Scheduled arrival should be before revised arrival')
        #
        # def clean__revised_departure(self):
        #     scheduled_departure = self.cleaned_data.get('scheduled_departure')
        #     revised_departure = self.cleaned_data.get('revised_departure')
        #
        #     if revised_departure < scheduled_departure:
        #         raise forms.ValidationError('Scheduled departure should be before revised departure')

        # def clean__booked_seats(self):
        #     total_seats = self.cleaned_data.get('total_seats')
        #     booked_seats = self.cleaned_data.get('booked_seats')
        #
        #     if booked_seats > total_seats:
        #         raise forms.ValidationError('Booked seats cannot be greater than total no of seats')


class CrewForm(forms.ModelForm):

    crew_id = forms.IntegerField(help_text="Enter a unique ID", label="ID")
    pilot = forms.BooleanField(help_text="Check for pilot, leave unchecked for crew", required=False)
    experience = forms.IntegerField(help_text="Enter experience in years")
    flights = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Flight.objects.active(),
                                             required=False, help_text="Select all flights where you work")

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


class AirlineForm(forms.ModelForm):

    name = forms.CharField(help_text="Enter a unique name")

    class Meta:
        model = Airline
        fields = [
            'name',
            'flight_prefix',
            'license_no',
            'no_of_aircrafts',
            'logo',
            'info',
        ]

        def clean__flight_prefix(self):
            flight_prefix = self.cleaned_data.get('flight_prefix')

            airline_qs = Airline.objects.get(flight_prefix=flight_prefix)
            if airline_qs.exists():
                raise forms.ValidationError("Airline with same prefix already exists")