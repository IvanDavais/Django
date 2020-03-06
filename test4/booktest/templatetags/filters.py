# 自定义过滤器
# 过滤器其实就是python函数
from django.template import Library

# 创建一个library函数
register = Library()

@register.filter
def mod(num):
    """ 判断num是否为偶数 """
    return num%2 == 0

@register.filter
def mod_val(num, val):
    return num%val == 0
