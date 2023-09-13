from .models import User, OfferWork
from django import forms
from phonenumber_field.formfields import PhoneNumberField, RegionalPhoneNumberWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    Name = forms.CharField(
        label="Name",
        max_length=100,
        error_messages={
            'required': 'Please enter your name.',
            'max_length': 'First name should not exceed 100 characters.'
        },
        widget=forms.TextInput(attrs={'class':'name-field', 'required':'true', 'placeholder':'Your Name'})
    )

    Phone = PhoneNumberField(
        label='Phone',
        region="UZ",
        error_messages = {
             'required': 'Please enter your phone number.',
             'invalid': 'Please enter a valid phone number.'
         },
         required = True,
         widget = RegionalPhoneNumberWidget(attrs={'placeholder': 'Your Phone Number'})
    )


class OfferWorkForm(forms.ModelForm):
    class Meta:
        model = OfferWork
        fields = '__all__'
