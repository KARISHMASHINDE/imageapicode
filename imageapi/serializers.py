from rest_framework import serializers
from django.contrib.auth.models import User
from .models import apiuser,imageprofile

class userSerializer(serializers.ModelSerializer):
    class Meta: 
        model = apiuser
        fields = ['user_name','Email']
        
        
class profileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = imageprofile
        fields = ['First_name','Last_name','Phone_no','image']