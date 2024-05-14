from django import template
from django_app import models

register = template.Library()


@register.filter()
def beauty_text(text,num_for_cut):
    if text > num_for_cut:
        return text[num_for_cut:]+'...'
    return text