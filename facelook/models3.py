from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
class User(models.Model):
    
    user_name = models.CharField(max_length = 20)
    username  = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    tel = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    
    def __str__(self):
    	return self.user_name

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
        return 'user favourite'

class  Image(models.Model):
    image_id = meta.AutoField('image id',primary_id=True) 
    image_local_path = models.CharField(max_length = 400)
    image_url = models.CharField(max_length = 400)
    zhi_user = models.ForeignKey(ZhiUser)
    zhi_answer = models.ForeignKey(Answer)
    insert_date = models

class Answer(models.Model):
    zhi_user_id
    question_title
    insert_date
    upvote
    downvote
    zhi_answer_id
    zhi_answer_url
    zhi_upvote
    zhi_answer_content

class ZhiUser(models.Model):
    user_url
    user_image
    sex
    nickname
    short_introduce
    long_introduce
    sina
