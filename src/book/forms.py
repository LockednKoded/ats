from django import forms
from.models import Album


class postform(forms.ModelForm):
    class Meta :
        model=Album
        fields=[
            "Room",
            "duration",
            "check_in",
            "check_out"


        ]

