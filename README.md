# Django_CRUD-->Function and Class Based
![profilecreate](https://github.com/Parvez49/Django_CRUD/assets/72366747/f1d1d652-fac2-48e3-a4a1-923dddce6af8)

# Run this Project
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
# Important Note-1 :
In model.py,
```
class genderChoice(models.TextChoices):
    choice1='m',"Male"
    choice2='f',"Female" # In Each choice: The first element is the actual value stored in the database, while the second element is the human-readable display value.

class Profile(models.Model):
    firstName=models.CharField(max_length=50,verbose_name="First Name",null=False)
    lastName=models.CharField(max_length=50,verbose_name="Last Name",null=True)
    age=models.IntegerField(null=True)
    dateOfBirth=models.DateField(null=True)
    gmail=models.EmailField(max_length=254,unique=True,verbose_name="Gmail")
    gender=models.CharField(max_length=1,choices=genderChoice.choices)
    profilePicture=models.ImageField(upload_to='Profile/Pictures/',max_length=50)
    cv=models.FileField(upload_to='Profile/Files/',max_length=50)
    shortVideo=models.FileField(upload_to='Profile/Video',max_length=50)
    description=models.TextField(max_length=500,null=True)
```
I used genderChoice class for definig choice list for gender feild in Profile model.
For Image or File setting, We have to set in setting.py by:
```
import os
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
```
and ProfileApp.urls
```
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```
So, any file will be stored in media directory. Suppose, profilePicture=models.ImageField(upload_to='Profile/Pictures/',max_length=50), for this feild image will be store in /media/Profile/Pictures/img.jpg

# Important Note-2 :
Notice that when we delete someting from database, django don't automatically delete associated file from media folder. To delete the associated files from the media folder when deleting a row from the database, we can manually delete the files using the delete method of the FieldFile or FileField objects.
```
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile

def confirmDelete(request, pk):
    prdata = Profile.objects.filter(pk=pk).first()

    if request.method == 'POST':
        if prdata:
            # Delete associated files from media folder
            if prdata.profilePicture:
                path = prdata.profilePicture.path
                if os.path.exists(path):
                    os.remove(path)

            if prdata.cv:
                path = prdata.cv.path
                if os.path.exists(path):
                    os.remove(path)

            if prdata.shortVideo:
                path = prdata.shortVideo.path
                if os.path.exists(path):
                    os.remove(path)

            # Delete the profile from the database
            prdata.delete()
            return redirect(reverse('profileapp:profile_list'))

    return render(request, 'profile/profile_confdelete.html', {'data': prdata})
```

# Important Note-3 :
In forms.py,
```
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
```
ProfileForm take all feild of Profile model by fields='__all__' . But we can add or some extra behavior in forms.
widgets add widgets in dateOfBirth feild. Initially all feild are required in forms. The __init__() section change this criteria. 
clean_cv() function make restiction only .pdf file only. similarly clean_profilePicture() restrict only jpg or png file only










