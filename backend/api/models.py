from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True) 
    profile_picture = models.URLField(blank=True, null=True)
    google_id = models.CharField(max_length=50, blank=True, null=True) 

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups', 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions', 
        blank=True,
    )


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [] 


#0 = plastic, 1 = playdoh, 2 = iron, 3 = bronze, 4 = silver, 5 = gold, 6 = 
class UserRank(models.Model):
    user = models.OneToOneField(to = User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])