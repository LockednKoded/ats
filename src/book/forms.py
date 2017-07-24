from django import forms
from .models import Book


class postform(forms.ModelForm):
    Categories = (
        ('AC', 'AC'),
        ('Non-AC', 'Non-AC')
    )
    Room = forms.ChoiceField(choices=Categories)
    check_in = forms.DateTimeField(help_text="Enter Field AS 2017-07-05 13:03:00")
    check_out = forms.DateTimeField(help_text="Enter Field AS 2017-07-05 13:03:00")

    class Meta:
        model = Book
        fields = [
            "Name",
            "Room",
            "contact_no",
            "check_in",
            "check_out"
        ]
