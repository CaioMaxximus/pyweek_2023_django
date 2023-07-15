from .filtros_customizados import replace_decimal_separator
from django import template

register = template.Library()
register.filter('replace_decimal_separator', replace_decimal_separator)

