from django import forms
from testing_app.models import  User
from testing_app.models import Contact
from testing_app.models import Job


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewUserForm(forms.ModelForm):
    class Meta():
        model= User
        fields='__all__'

class ApplyNowForm(forms.ModelForm):
    class Meta():
        model= Job
        fields='__all__'
