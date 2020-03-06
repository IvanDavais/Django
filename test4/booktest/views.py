from django.shortcuts import render,redirect
from django.http import HttpResponse
from booktest.models import BookInfo

# Create your views here.

def login_required(view_func):
    """ 登陆状态判断装饰器 """

    def wrapper(request, *view_args, **view_kwargs):
        """ 判断用户是否登陆 """
        if request.session.has_key('islogin'):
            # 用户已经登陆，吊桶对应的视图
            return view_func(request,*view_args,**view_kwargs)
        else:
            # 用户未登陆
            return redirect('/login')
    return wrapper

def temp_var(request):
    my_dict = {'title': '字典键值'}
    my_list = [1,2,3]
    book = BookInfo.objects.get(id=1)

    # 定义模版上下文
    context = {'my_dict':my_dict, 'my_list':my_list, 'book':book}
    return render(request,'booktest/temp_var.html',context)

def temp_tags(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/temp_tags.html',{'books':books})

def temp_filter(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/temp_filter.html',{'books':books})

def base(request):
    return render(request,'booktest/base.html')

def child(request):
    return render(request,'booktest/child.html')

def html_escape(request):
    """ html转义 """
    return render(request,'booktest/html_escape.html',{'content':'<h1>hello Fan</h1>'})

# /login
def login(request):
    """ 登陆页面 """
    
    # 判断用户是否已经登陆，如果已经登陆则直接返回首页
    if request.session.has_key('islogin'):
        return redirect('/change_pwd')
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

    # 获取用户输入验证码
    vcode1 = request.POST.get('vcode')
    # 获取系统生成的验证码，保存在session中
    vcode2 = request.session.get('verifycode')

    if vcode1 != vcode2:
        return redirect('/login')

    # 进行登陆的校验，模拟用户名为smart，密码:123
    if username == 'smart' and password == '123':
    # 因为设置cookie需要一个HttpResponse类的对象，或者它字累的对象注意redirect
    # 此处的redirect的返回值就是HttpResponseRedirect对象，
    # 而HttpResponseRedict就是HttpResponse的子类。
        response = redirect('/change_pwd')
        if remember == 'on':
            # 设置cookie username， 过期时间为两周
            response.set_cookie('username',username,max_age=7*24*3600) 
        
        # 只要session中有islogin，就认为用户已经登陆
        # 注意不是用户非要点了记录用户名才能设置session，session的目的是记录用户的登陆状态
        request.session['islogin'] = True
        request.session['username'] = username

        return response
    else:
        return redirect('/login')

@login_required
def change_pwd(request):
    """ 显示修改密码页面 """
    
    # 进入修改密码页前，先判断用户是否已经登陆了
    # if not request.session.has_key('islogin'):
        # return render(request,'booktest/login.html')
    return render(request,'booktest/change_pwd.html')

@login_required
def change_pwd_action(request):
    """ 密码修改成功页面 """
    
    # 进入修改密码页前，先判断用户是否已经登陆了
    # if not request.session.has_key('islogin'):
        # return render(request,'booktest/login.html')
    
    # 获取新密码
    username = request.session['username']
    pwd = request.POST.get('pwd')
    # 实际开发的时候，修改数据库中对应的内容
    # 返回一个应答
    return HttpResponse('%s 用户修改后的密码为: %s' %(username, pwd))



# image:图片类，ImageDraw:画图片的类，ImageFont: 图片上的字体类
from PIL import Image, ImageDraw, ImageFont
# BytesIO:操作内存文件的类
from django.utils.six import BytesIO
 
# /verify_code
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色 （即产生三个随机数，构成 RGB的颜色表示方式)
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    # 宽
    width = 100
    # 高
    height = 25
    # 创建画布对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # xy构成一个点的坐标，（x,y）表示你要在哪个点画颜色，点的颜色是fill
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('/System/Library/Fonts/Avenir.ttc', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作（把画好的验证码存到内存文件中）
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端（浏览器），MIME类型为图片png（并告诉浏览器你返回的是png格式的图片）
    return HttpResponse(buf.getvalue(), 'image/png')