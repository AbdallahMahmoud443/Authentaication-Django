from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.


# class CustomUser(AbstractUser): # AbstractUser => is defualt User Class That Defined By Django
#       COUNTRY_CHOICES = [
#          ('US', 'United States'),
#          ('UK', 'United Kingdom'),
#          ('IN', 'India'),
#          ('AU', 'Australia'),
#         ]
#       country = models.CharField(choices=COUNTRY_CHOICES,max_length=2)
#       address = models.CharField(max_length=30,blank=True)


class CustomPermissions(models.Model):
    #! Create one to one between CustomPermissions and Permission type is important (customPermission type)
    permissions = models.OneToOneField(Permission,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return self.permissions.name
    
    class Meta:
        permissions =(
            ('add_staff','can add stuff user'), # (codeName,name)
            ('update_staff','Can edit stuff user'),
            ('view_staff','can view stuff users'),
            ('delete_staff','can delete stuff users'),
        )
    
    
    
    