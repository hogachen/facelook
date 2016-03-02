#encoding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from facelook.models import User
from facelook.models import Image

#返回json格式数据
def get_user(user_id):
    user_msg = User.objects.filter(id=user_id)
    if len(user_msg)==0:
        return -1
    return user_msg[0]


#获取最新资源
def get_newest_page_lib(date='00000000',page=0):
    
    print date,page
    step = 2
    si = 0
    ei = step
     
    if page != 0:
        si = (page)*step
        ei = (page + 1) * step

    image_list = Image.objects.all()[si:ei]
    if date != '00000000':
        image_list = Image.objects.filter(insert_date=date)[si:ei]
        
    json_str = []
    for image in image_list:
        image_dic = {}
        image_dic['image_id'] = image.image_id
        image_dic['image_local_path'] = image.image_local_path
        image_dic['image_url'] = image.image_url
        image_dic['insert_date'] = image.insert_date
        image_dic['zhi_answer_id'] = image.zhi_answer_id
        image_dic['zhi_user_id'] = image.zhi_user_id
        json_str.append(image_dic)
    return json_str

