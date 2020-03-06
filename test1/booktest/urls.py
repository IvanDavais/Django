from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 通过url函数设置url路由配置项
        url(r'^index$',views.index),   
        url(r'^books$',views.show_books),   # 显示图书信息  
        # 注意此处\d+需要用()包住，不然无法向views中的detail函数传递bid参数，
        # ()叫做正则表达式的组，django会把正则表达式的组中的值作为参数传递
        url(r'^books/(\d+)$',views.detail), #显示图书对应的英雄的具体信息
    ]
