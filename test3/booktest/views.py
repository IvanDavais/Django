from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime,timedelta

# Create your views here.
def index(request):
    """ 首页 """
    # num = 'a' + 1
    return render(request,'booktest/index.html')

def show_arg(request,num):
    return HttpResponse(num)

# /login
def login(request):
    """ 登陆页面 """
    
    # 判断用户是否已经登陆，如果已经登陆则直接返回首页
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        # 判断用户是否点击过记住密码按钮
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        #注意字典的正确写法{value:key} 
        return render(request,'booktest/login.html',{'username':username})

# /login_check
def login_check(request):
    # 获取用户名，密码，是否需要记住用户名
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remember)
    # console.log(username+'\n'+password)

    if username == 'smart' and password == '123':
    # 因为设置cookie需要一个HttpResponse类的对象，或者它字累的对象注意redirect
    # 此处的redirect的返回值就是HttpResponseRedirect对象，
    # 而HttpResponseRedict就是HttpResponse的子类。
        response = redirect('/index')
        if remember == 'on':
            # 设置cookie username， 过期时间为两周
            response.set_cookie('username',username,max_age=7*24*3600) 
            # 只要session中有islogin，就认为用户已经登陆
            request.session['islogin'] = True
        return response
    else:
        return redirect('/login')

def ajax_test(request):
    """ 显示ajax页面 """
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    """ 返回的json数据{'res':1} """
    return JsonResponse({'res':1})

def login_ajax(request):
    """ 显示ajax登陆页面 """
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):
    """ ajax登陆校验 """
    # 获取用户名和密码(注意无论是表单post提交还是ajax的post提交都可以使用下面语句)
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 进行校验，返回json数据
    if username == 'smart' and password == '123':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

#  /set_cookie
def set_cookie(request):
    """ 设置cookie信息 """
    Response = HttpResponse('设置cookie')
    # 设置一个cookie信息，名字为num，值为1
    # Response.set_cookie('num',1)
    Response.set_cookie('num',1,max_age=60*60*24)

    # 返回response
    return Response

#  /get_cookie
def get_cookie(request):
    """ 获取cookie信息 """
    num = request.COOKIES['num']
    return HttpResponse(num)

# /set_session
def set_session(request):
    """ 设置session """
    request.session['username'] = 'smart'
    request.session['age'] = 18;
    return HttpResponse('设置session')

# /get_session
def get_session(request):
    """ 获取session """
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))

# clear_session
def clear_session(request):
    """ 清除session信息 """
    request.session.clear()
    return HttpResponse('session清除成功！')