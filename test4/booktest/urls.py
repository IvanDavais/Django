from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 注意正则表达式前后一定要加'^','$'
    url(r'^temp_var$', views.temp_var), #模版变量
    url(r'^temp_tags$', views.temp_tags),
    url(r'^temp_filter$',views.temp_filter),
    url(r'^base$', views.base),
    url(r'^child$', views.child),
    url(r'^html_escape$',views.html_escape),
    url(r'login$',views.login),
    url(r'^login_check$',views.login_check),
    url(r'^change_pwd$',views.change_pwd),
    url(r'^change_pwd_action$',views.change_pwd_action),
    url(r'^verify_code$', views.verify_code),

]