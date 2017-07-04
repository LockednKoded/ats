from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):  # *args, **kwargs to handle any additional arguments that may be passes
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Your login credentials are incorrect')
            if not user.check_password(password):  # not required, since authenticate checks both, but just in case
                raise forms.ValidationError('Your password is incorrect')
            if not user.is_active:  # not required, authenticate also checks for this
                raise forms.ValidationError("This user is no longer active")

        return super(LoginForm, self).clean()  # clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):

    USER_TYPE = (
        (1, 'Traveller'),
        (2, 'Employee'),
    )

    email = forms.EmailField(label="Email Address")
    # writing email  here, to make make email required*, username and password are required by default
    email2 = forms.EmailField(label="Confirm Email")
    # writing password here to make its field type to password
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    register_type = forms.ChoiceField(choices=USER_TYPE, label="You are a")

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'email',
            'email2',
            'register_type',
        ]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            print("Password mismatch")
            # TODO: Here this validation error is not being raised
            return forms.ValidationError("The two passwords don't match")
        else:
            print("passwords matched")
        return password

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")

        if email != email2:
            raise forms.ValidationError("Emails must match")
        else:
            print("Emails matched")
        return email


class TravellerProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'contact_no',
            'photo',
            'ticket_no',
            'flight_no',
        ]


class EmployeeProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'contact_no',
            'photo',
        ]