
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
    def clean_cv(self):
        cv_file = self.cleaned_data.get('cv')
        if cv_file:
            # Check if the file extension is not .pdf
            if not cv_file.name.endswith('.pdf'):
                raise ValidationError("Only PDF files are allowed for the CV field.")
        return cv_file
    
    def clean_profilePicture(self):
        profile_picture = self.cleaned_data.get('profilePicture')
        if profile_picture:
            # Check if the file extension is not .png or .jpg
            if not profile_picture.name.lower().endswith(('.png', '.jpg')):
                raise ValidationError("Only PNG and JPG files are allowed for the profile picture field.")
        return profile_picture
