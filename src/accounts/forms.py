from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):  # *args, **kwargs to handle any additional arguments that may be passed
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

        return super(LoginForm, self).clean()  # can write clean(*args,**kwargs) #call the clean method of the super class


class RegisterForm(forms.ModelForm):

    USER_TYPE = (
        (1, 'Traveller'),
        (2, 'Employee'),
    )

    # writing email  here, to make make email required*, username and password are required by default
    email = forms.EmailField(label="Email Address")
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

# We don't want other details (not mentioned in fields below) to be edited by the respective users
# Those details will be added/edited by the admin (though admin panel)


class TravellerProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        # fields list all model field that will be displayed in the form as well as decides their order
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