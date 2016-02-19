from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
class User(models.Model):
    
    user_name = models.CharField(max_length = 20)
    user_desc = models.CharField(max_length = 200)
    
    def __str__(self):
    	return self.user_desc

class UserMsg(models.Model):

    user = models.ForeignKey(User)
    msg_title = models.CharField(max_length = 200)
    user_msg = models.CharField(max_length = 200)
    def __str__(self):
    	return self.user_msg
    
