from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


STATE = (('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
         ('Andhra Pradesh', 'Andhra Pradesh'),
         ('Arunachal Pradesh', 'Arunachal Pradesh'),
         ('Assam', 'Assam'),
         ('Bihar', 'Bihar'),
         ('Chandigarh', 'Chandigarh'),
         ('Chattisgarh', 'Chattisgarh'),
         ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
         ('Daman and Diu', 'Daman and Diu'),
         ('Delhi', 'Delhi'),
         ('Goa', 'Goa'),
         ('Gujarat', 'Gujarat'),
         ('Haryana', 'Haryana'),
         ('Himachal Pradesh', 'Himachal Pradesh'),
         ('Jammu and Kashmir', 'Jammu and Kashmir'),
         ('Jharkhand', 'Jharkhand'),
         ('Karnataka', 'Karnataka'),
         ('Kerala', 'Kerala'),
         ('Lakshadweep', 'Lakshadweep'),
         ('Madhya Pradesh', 'Madhya Pradesh'),
         ('Maharashtra', 'Maharashtra'),
         ('Manipur', 'Manipur'),
         ('Meghalaya', 'Meghalaya'),
         ('Mizoram', 'Mizoram'),
         ('Nagaland', 'Nagaland'),
         ('Odisha', 'Odisha'),
         ('Puducherry', 'Puducherry'),
         ('Punjab', 'Punjab'),
         ('Rajasthan', 'Rajasthan'),
         ('Sikkim', 'Sikkim'),
         ('Tamil Nadu', 'Tamil Nadu'),
         ('Telangana', 'Telangana'),
         ('Tripura', 'Tripura'),
         ('Uttar Pradesh', 'Uttar Pradesh'),
         ('Uttarakhand', 'Uttarakhand'),
         ('West Bengal', 'West Bengal'),
         )


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    Pincode = models.IntegerField(null=True)
    State = models.CharField(choices=STATE, max_length=100)
    profile_pic = models.FileField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return str(self.id)
