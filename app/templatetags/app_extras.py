import datetime
from django import template

register = template.Library()

@register.inclusion_tag('app/rating_display_tag.html')
def rating_display_tag(rating):
	return {
		"rating": rating,
		"stars": range(1, rating+1)
	}