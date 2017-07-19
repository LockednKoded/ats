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

    def clean_flight_no(self):
        flight_no = self.cleaned_data.get('flight_no')

        flights_qs = Flight.objects.filter(flight_no=flight_no)
        if flights_qs.exists():
            raise forms.ValidationError("Flight with this no already exists")

        return flight_no

    def clean_days_operational(self):
        days_operational = self.cleaned_data.get('days_operational')

        if len(days_operational) == 0:
            raise forms.ValidationError('Flight should be scheduled for atleast one day')

        return days_operational

    def clean(self):
        scheduled_arrival = self.cleaned_data.get('scheduled_arrival')
        scheduled_departure = self.cleaned_data.get('scheduled_departure')
        revised_arrival = self.cleaned_data.get('revised_arrival')
        revised_departure = self.cleaned_data.get('revised_departure')

        if revised_arrival < scheduled_arrival:
            raise forms.ValidationError('Scheduled arrival should be before revised arrival')
        if revised_departure < scheduled_departure:
            raise forms.ValidationError('Scheduled departure should be before revised departure')

        total_seats = self.cleaned_data.get('total_seats')
        booked_seats = self.cleaned_data.get('booked_seats')

        if booked_seats > total_seats:
            raise forms.ValidationError('Booked seats cannot be greater than total seats')

        origin = self.cleaned_data.get('origin')
        destination = self.cleaned_data.get('destination')

        if origin == destination:
            raise forms.ValidationError('Origin and destination for flight cannot be same')

        return super(FlightForm, self).clean()


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

    def clean_crew_id(self):
        crew_id = self.cleaned_data.get('crew_id')

        crew_qs = Crew.objects.filter(crew_id=crew_id)
        if crew_qs.exists():
            raise forms.ValidationError("Crew with same id already exists")

        return crew_id


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

    def clean_flight_prefix(self):
        flight_prefix = self.cleaned_data.get('flight_prefix')

        airline_qs = Airline.objects.filter(flight_prefix=flight_prefix)
        if airline_qs.exists():
            raise forms.ValidationError("Airline with same prefix already exists")

        return flight_prefix

    def clean_name(self):
        name = self.cleaned_data.get('name')

        airline_qs = Airline.objects.filter(name=name)
        if airline_qs.exists():
            raise forms.ValidationError("Airline with same name already exists")

        return name
