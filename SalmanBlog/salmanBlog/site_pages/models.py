from django.db import models

# Create your models here.
class Admin_info(models.Model):
    full_name = models.CharField(max_length= 255)
    profession = models.CharField(max_length= 255)
    avatar = models.ImageField(upload_to = 'media/')
    bio = models.TextField()
        
        
    def __str__(self):
        return "Admin Info"