from django import forms

from .models import Flight, security_forces, force_employee


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
            'approved_plan',
            'operation_days'

        ]



        def clean__flight_no(self):
            flight_no = self.cleaned_data.get('flight_no')

            flights_qs = Flight.objects.get(flight_no=flight_no)
            if flights_qs.exists():
                raise forms.ValidationError("Flight with same no. already exists")




class force_Form(forms.ModelForm):

    employee_id = forms.IntegerField(help_text="Enter a unique ID", label="ID")

    experience = forms.IntegerField(help_text="Enter experience in years")

    class Meta:
        model = force_employee
        fields = [
            'employee_id',
            'name',
            'force',
            'experience',
            'license_no',
            'ph_no',
            'in_service',

        ]

        def clean__employee_id(self):
            employee_id = self.cleaned_data.get('employee_id')

            crew_qs = force_employee.objects.get(employee_id=employee_id)
            if crew_qs.exists():
                raise forms.ValidationError("Crew with same id already exists")


class AirlineForm(forms.ModelForm):

    name = forms.CharField(help_text="Enter a unique name")

    class Meta:
        model = security_forces
        fields = [
            'name',
            'license_no',

        ]

