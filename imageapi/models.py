from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class apiuser(models.Model):
    user_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.user_name


    
    
class imageprofile(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    Phone_no = models.IntegerField(default=True)
    def __unicode__(self):
        return self.First_name
    
    
# def image_img(self):
#     if self.item_image:
#         return u'<img src="%s" width="50" height="50" />' % self.image.url
#     else:
#         return '(Sin imagen)'
# image_img.short_description = 'Thumb'
# image_img.allow_tags = True
    
    


    