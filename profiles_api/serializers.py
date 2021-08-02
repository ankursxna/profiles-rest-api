from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    age  = serializers.CharField(max_length=5)



# As far as I can understand, serializers are similar to a 'input' statements we use in Python.
# Or we can compare this with a text or other input fields we use Tkinter as well.
# So in short, we will have a field with 'Name' header where a user can insert values inside the field.
# And we are allowing user to insert value with maximum 10 characters length.

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfiles
        # To work with ModelSerializer we need to define this meta class so that we can ...
        # ... point our serializer to specific model in our project.
        # Below we will list down fields that we want to manage with our serializer
        fields = ('id','email','name','password')
        # However we need to make an exception with password field as we only want to update ...
        # ... password when creating a new user and for the rest of time we wont allow a user to retrieve the password back
        # by using HTTP GET method. We will solve this problem by defining keyword arguments or shotform 'kwargs'
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
        # [1] - Here I believe all these variables defined are keywords for ModelSerializer like ...
        # ... fields, extra_kwargs, write_only, style, input_type. If they aren't keywords then we would require to pass them ...
        # ... into some function to set all these things.
        # [2] - For password we set write_only as True this means, we can create or update the password but can not read it.
        # [3] - We have set style's input_type as 'password' so that when creating or updating password, it should be ...
        # ... displayed as hash or masked stars.

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfiles.objects.create_user(
            email    = validated_data['email'],
            name     = validated_data['name'],
            password = validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model  = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
