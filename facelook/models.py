
#encoding:utf-8
import models
import json
from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
class User(models.Model):
    
    user_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 200)
    tel = models.CharField(max_length = 200, default='10086')
    password = models.CharField(max_length = 200)
    
    def __str__(self):
        jsonString = []
        attr={}
        attr['user_name'] = self.user_name
        attr['email'] = self.email
        attr['tel'] = self.tel
        attr['password'] = self.password
        jsonString.append(attr)
        return json.dumps(jsonString)       

class Answer(models.Model):
    answer_id = models.CharField(max_length=100)
    zhi_user_id = models.CharField(max_length=100)
    question_title = models.CharField(max_length = 300)
    insert_date = models.DateField() 
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    zhi_answer_id = models.IntegerField()
    zhi_answer_url = models.CharField(max_length=100)
    zhi_upvote = models.IntegerField() 
    zhi_answer_content = models.CharField(max_length=1000)
    
class ZhiUser(models.Model):
    zhi_user_id = models.CharField(max_length=200)
    user_url = models.CharField(max_length = 300)
    user_image = models.CharField(max_length=200)
    sex = models.CharField('性别',max_length = 10)  
    nickname = models.CharField('昵称',max_length = 100)    
    short_introduce = models.CharField('短介绍',max_length = 200)
    long_introduce = models.CharField('长介绍',max_length = 400)    
    sina = models.CharField('新浪微博',max_length = 40)

class  Image(models.Model):
    image_id = models.CharField(max_length=100) 
    image_local_path = models.CharField(max_length = 400)
    image_url = models.CharField(max_length = 400)
    zhi_user = models.ForeignKey(ZhiUser)
    zhi_answer = models.ForeignKey(Answer)
    insert_date = models.DateField()

    def __str__(self):
        return self.image_id

class UserFavourite(models.Model):
    
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    def __str__(self):
        return 'user favourite'

class UserCollect(models.Model):
    
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    def __str__(self):
        return 'user collect'
