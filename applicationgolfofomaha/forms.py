from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserCreated, SlotBooking, Event
from django.forms import ModelForm, DateInput


class UserCreateForm(UserCreationForm):
    CHOICES = [('golfofomahauser','golfofomahauser'),
               ('admin', 'admin')]
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["role"]
        if commit:
            user.save()
        return user


class CustomerForm(forms.ModelForm):
    class Meta:
        model = UserCreated
        fields = ('cust_name', 'phone_number')


class SlotbookingForm(forms.ModelForm):
    class Meta:
        model = SlotBooking
        fields = ('event', 'timeslot','bookingdate')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'start_time')
