from django import forms
from .models import Contact # Ensure Contact model exists
from .models import Event

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']  # Ensure these fields exist in Contact model


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Event  # Ensure Event model is correctly imported
        fields = ['name', 'email', 'phone_number']  # Adjust as needed