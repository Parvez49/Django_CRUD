from django.db import models

# Create your models here.

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

