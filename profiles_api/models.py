from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Above two libs required as base classes when we need to modify the default authentication settings of django.
# Below we will create a UserProfiles class and will pass the above base classes.
# Hence as per OOPs Concepts, all the attributes of these two classes will be inheritied by the class we will create.

class UserProfileManager(BaseUserManager):
    """"Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        # [1] - This normalize_email is being inheritied from 'BaseUserManager' which is the default user manager of Django.
        # [2] - normalize_email will lowercase the domain portion of the email address.
        # Doc Link : https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email
        user  = self.model(email=email, name=name)
        user.set_password(password)
        # [1] - set_password is inheritied from AbstractBaseUser
        # [2] - This is done so that password is not saved as plain text instead saved as masked hashed characters for security.
        user.save(using=self._db)  # this is standard way of saving objects in Django and is described in official Django docs.

        return user

        def create_superuser(self, email, name, password):
            """Create and save a new superuser with given details"""
            user = self.create_user(email, name, password)
            user.is_superuser = True
            user.is_staff     = True
            user.save(using=self._db)

            return user 




class UserProfiles(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True) # Means no two users will have same email as unique=True.
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # This means by default all users will be active users
    is_staff  = models.BooleanField(default=False) # This means by default all user will NOT be staff users.

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'   # Means we are overwriting the default Django settings of asking for username for authentication.
    REQUIRED_FIELDS  = ['name']
    # Means along with the main authentication field 'email', we also need fields part of this list as required fields when user creates his profile.

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
        # NOTE : To understand what is __str__, check the Jupyter Notebook 'Python - Basic Programming' under header 'Use of str() in a class'
