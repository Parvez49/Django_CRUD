
from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model= Profile
        fields='__all__'
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'})
        }
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['lastName'].required = False
        self.fields['age'].required = False
