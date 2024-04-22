from django import template
from django_app import models

register = template.Library()

@register.simple_tag()
def beauty_number(num):
    num = str(num)
    for i in range(len(num)-3,-1,-3):
        num = num[:i] +' '+num[i:]
    return num

@register.filter()
def beauty_text(text,num_for_cut):
    if text > num_for_cut:
        return text[num_for_cut:]+'...'
    return text