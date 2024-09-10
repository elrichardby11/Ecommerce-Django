from django import template

register = template.Library()

@register.filter
def format_clp(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    
    return f"${value:,.0f}".replace(',', '.')
