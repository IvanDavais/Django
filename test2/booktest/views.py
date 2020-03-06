from django.shortcuts import render,redirect
from booktest.models import BookInfo,AreaInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    # 查询出所有的图书信息
    books = BookInfo.objects.all()
    # 使用模版
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑1'
    b.bpub_date = date(2020,1,1)
    b.save()
    # 返回应答，让浏览器在访问首页 
    # return HttpResponse('ok')
    # return HttpResponseRedirect('/index')
    return redirect('/index') 

def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    # return HttpResponseRedirect('/index')
    return redirect('/index')

def areas(request):
    area = AreaInfo.objects.get(atitle='广州市')
    # 查询广州市的上级地区
    parent = area.aParent
    # 查询广州市的下级地区
    children = area.areainfo_set.all()
    # 使用模版
    return render(request,'booktest/areas.html',{"area":area, "parent":parent, "children":children})