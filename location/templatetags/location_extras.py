from django import template

register = template.Library()

@register.filter
def post_page_num(value, page_num=None):
	page_volume = (page_num-1)*500
	return value + page_volume
