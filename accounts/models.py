from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        if not name:
            raise ValueError('Please enter your name')

        user = self.model(
            email=self.normalize_email(email),
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        print('Base user created')
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_images', default='user.png')
    location = models.CharField( max_length=100, blank=True, null=True)
    organizer = models.BooleanField(default=False)
    instagram = models.CharField(max_length=100, blank=True, null=True) 
    twitter = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["-name"]
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    
    @property
    def is_organizer(self):
         # "Is the user organizer?"
         return self.organizer
    
    objects = CustomUserManager()


