



from django.db import models
# Create your models here.
import datetime
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
    
class UserFavourite(model.Model):
    
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    def __str__(self):
        return self.user.user_name

class  Image(models.Model):
    
    image_local_path = models.CharField(max_length = 400)
    image_url = models.CharField(max_length = 400)
    zhi_user_id
    zhi_answer_id
    answer = models.ForeignKey(Answer)
    insert_date = models
