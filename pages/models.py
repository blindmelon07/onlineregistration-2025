from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    f_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    branch_name = models.CharField(max_length=100)
    is_registered = models.BooleanField(default=False)




    def __str__(self):
        return f"{self.f_name}"