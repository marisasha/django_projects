from django import template

register = template.Library()

@register.filter(name="custom_cut")
def custom_cut(text: any, length: int) -> str:
    if len(str(text)) > length:
        return str(text)[:length] + "..."
    return str(text)

@register.simple_tag()
def beauty_number(num):
    num = str(num)
    for i in range(len(num)-3,-1,-3):
        num = num[:i] +' '+num[i:]
    return num

