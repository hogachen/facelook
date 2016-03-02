#encoding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from facelook.models import User
from facelook.models import Image
from facelook.models import UserFavourite
from facelook.models import UserCollect
def index(request):
    return HttpResponse('you are in index')
#返回json格式数据
def get_user(request,user_id):
    print 'in get_user'
    user_msg = User.objects.filter(id=user_id)
    if len(user_msg)==0:
        return HttpResponse(-1)
    return HttpResponse(user_msg[0])


#获取最新资源
def get_newest_image(request,user_id,select_date=0,select_page=0):
    print select_date,select_page
     
    step = 2
    si = 0
    ei = step
     
    select_page = int(select_page)
    if select_page != 0:
        si = (select_page)*step
        ei = (select_page + 1) * step

    image_dic = Image.objects.all()[si:ei]
    if select_date != '0':
        image_dic = Image.objects.filter(insert_date=select_date)[si:ei]
        
    json_str = []
    for image in image_dic:
        image_dic={}
        image_dic['image_id'] = image.image_id
        image_dic['image_local_path'] = image.image_local_path
        image_dic['image_url'] = image.image_url
        image_dic['insert_date'] = image.insert_date
        image_dic['zhi_answer_id'] = image.zhi_answer_id
        image_dic['zhi_user_id'] = image.zhi_user_id
        
        collect = get_image_collect(user_id,image_id)
        image_dic['collect'] = collect
        faviour_count = get_image_faviour_count(user_id,image_id)
        image_dic['faviour_count'] = faviour_count
        json_str.append(image_dic)
    return  HttpResponse(json_str)
"""
插入用户注册信息
"""
def register(request, user_name, email,tel, password):
    user_mail = User.objects.filter(email=email)
    if len(user_mail) > 0:
        return HttpResponse(-1)
    new_user = User(user_name=user_name,email=email,tel=tel, password=password)
    new_user.save()
    return HttpResponse(1)
    
"""
用户登录
"""
def login(request, email, password):
    user_login = User.objects.filter(email=email).values()
    db_password = User.objects.filter(email=email)[0].password
    if len(user_login) == 1 and db_password == password:
        return HttpResponse(user_login)
    return HttpResponse(-1)


"""
取出点赞总数
"""
def get_image_faviour_count(image_id):
    faviour_count = UserFavourite.objects.filter(image_id=image_id).count()
    return faviour_count
    pass
    
"""
取出该用户是否收藏了图片
"""
def get_image_collect(user_id, image_id):
    is_collect = Collect.objects.filter(user_id=user_id,image_id=image_id).count()
    if is_collect == 1:
        return 1
    return 0
    pass

"""
插入点赞
"""
def insert_faviour(request,user_id, image_id):
    user = User.objects.filter(id=user_id)
    image = Image.objects.filter(image_id=image_id)

    favourite = UserFavourite.objects.filter(user=user[0],image=image[0])
    
    if len(favourite) <=0 and len(user)>0 and len(image)>0:
        favourite = UserFavourite(user=user[0],image=image[0])
        favourite.save()
        return HttpResponse(1)
    return HttpResponse(-1)
"""
插入收藏
"""
def insert_collect(request, user_id, image_id):
    user = User.objects.filter(id=user_id)
    image = Image.objects.filter(image_id=image_id)
    collect = UserCollect.objects.filter(user=user[0],image=image[0])

    if len(collect) <=0 and len(user)>0 and len(image)>0:
        collect = UserCollect(user=user[0],image=image[0])
        collect.save()
        return HttpResponse(1)
    return HttpResponse(-1)
"""
根据image_id获取一张图片所有内容
"""
def get_one_image(user_id, image_id):
    image_set = Image.objects.filter(image_id=image_id)
    image_dic = {}
    if len(image) ==1:
        image = image_set[0]
        image_dic['image_id'] = image.image_id
        image_dic['image_local_path'] = image.image_local_path
        image_dic['image_url'] = image.image_url
        image_dic['insert_date'] = image.insert_date
        image_dic['zhi_answer_id'] = image.zhi_answer_id
        image_dic['zhi_user_id'] = image.zhi_user_id
        
        collect = get_image_collect(user_id,image_id)
        image_dic['collect'] = collect
        faviour_count = get_image_faviour_count(user_id,image_id)
        image_dic['faviour_count'] = faviour_count
        return image_dic
    

"""
取出用户收藏列表
"""
def get_user_collect_list(request, user_id):
    collect_list = UserCollect.objects.filter(user_id=user_id)
    image_list = []
    for collect in collect_list:
        image_id = collect.image.image_id
        image = get_one_image(user_id, image_id)
        image_list.append(image)
    return HttpResponse(image_list)

