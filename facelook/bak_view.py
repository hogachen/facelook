from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from facelook.models import User
from facelook.models import UserMsg

#返回json格式数据
def get_user(request,user_id):
    user_msg = User.objects.all().get(id=user_id)
    user_name = user_msg.objects.get(user_name)
    return HttpResponse(user_name)





def index(request):
    return HttpResponse("Hello, world. You're at the facelook index.")

def user_desc(request):
    user_list = User.objects.all()
    template = loader.get_template('facelook/user_desc.html')
    context = RequestContext(request,{'user_list':user_list})
    return HttpResponse(template.render(context))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def user_desc_detail(request, user_name):
    user = User.objects.all().get(user_name=user_name)
    print user.user_name
    user_desc = user.user_desc
    response = "the people is description as %s." 
    return HttpResponse(response  % user_desc)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
