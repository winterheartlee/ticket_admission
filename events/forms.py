from django import forms
from .widgets import CustomClearableFileInput
from .models import Event
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    # using attrs to send type:datetime-local for HTML5 datetime picker
    starts = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    ends = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    user = forms.CharField(widget=forms.TextInput(attrs={'id': 'user','type': 'hidden'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    