from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo # 导入图书模型类

# Create your views here.
# 1.定义视图函数，request是HTTPRequest中的一个对象
# 2.进行url配置，建立url地址和视图的对应关系 
def index(request):
    # 进行处理，和M和T进行交互，此处省略，后面会讲
    # return HttpResponse('Hello Fan!')

    # 使用模版文件
    # 1.加载模版文件
    # temp = loader.get_template('booktest/index.html')
    # # 2.定义模版上下文：给模版文件传递数据
    # context = RequestContext(request,{})
    # # 3.模版渲染：产生标准的html内容
    # res_html = temp.render(context)
    # # 4. 返回给浏览器
    # return HttpResponse(res_html)
    # return render(request,'booktest/index.html',context=None)
    return render(request,'booktest/index.html',{'content':'通过字典传过来的参数','list': list(range(1,9,2))})
    
# def my_render(requset, template_path, context_dict={}):
#     """封装上面的函数"""
#     temp = loader.get_template(template_path)
#     context = RequestContext(request,context_dict)w
#     res_html = temp.render(context)

def show_books(request):
    """ 显示图书的信息 """
    # 1.通过M从数据库中查找图书表中的数据 
    books = BookInfo.objects.all() #查阅图书表中的所有内容  
    # 2. 使用模版
    return render(request,'booktest/show_books.html',{'books':books})


def detail(request,bid):
    """ 查询图书关联的图书信息 """
    # 1. 根据bid查询图书id
    book = BookInfo.objects.get(id=bid)
    # 2. 查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 使用模版，将数据传递给模版，进行展示
    return render(request,'booktest/detail.html',{'book':book,"heros":heros})