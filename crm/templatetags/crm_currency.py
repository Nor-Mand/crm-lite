from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


def currency(dollar):
    dollar = round(float(dollar), 2)
    return '$%s%s' % (intcomma(int(dollar)), ("%0.2f" % dollar)[-3:])

register.filter('currency', currency)