from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Appointment, User

class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', required=True)
    address = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            msg = "Passwords do not match"
            self.add_error('password', msg)


class LoginForm(forms.Form):
    email_or_phone = forms.CharField(label='Email or Phone', required=True)
    password = forms.CharField(required=True)


class TutorCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', required=True)
    avatar = forms.ImageField(label='Upload Image', required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'confirm_password', 'description', 'avatar']
        image = CloudinaryFileField(
            options = { 
                'tags': "directly_uploaded",
                'crop': 'limit', 'width': 250, 'height': 250,
                'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
        })

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            msg = "Passwords do not match"
            self.add_error('password', msg)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        read_only_fields = ['status', 'time_created', 'date_created', 'user', 'name', 'email']
        fields = '__all__'