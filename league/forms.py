from django import forms
from django.forms import ModelForm
from login.models import Regulation
from django.forms import widgets
import datetime
from django.core.exceptions import ValidationError
from datetime import date

class RegulationForm(forms.ModelForm):
    class Meta:
        model = Regulation
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # Add Bootstrap classes to form labels
    def label_tag(self, label=None, attrs=None, label_suffix=None):
        attrs = attrs or {}
        attrs['class'] = 'form-label'
        return super().label_tag(label, attrs, label_suffix)
    
    def clean(self):
        cleaned_data = super().clean()
        winpts = cleaned_data.get('winpts')
        losepts = cleaned_data.get('losepts')
        drawpts = cleaned_data.get('drawpts')
        if winpts < drawpts or winpts < losepts:
            self.add_error('winpts', "Win points must be greater than lose points and draw points")
        if drawpts < losepts or drawpts > winpts:
            self.add_error('drawpts', "Draw points must be greater than lose points and lower than win points")
        if losepts > drawpts or losepts > winpts:
            self.add_error('losepts', "Lose points must be lower that draw points and win points") 
        