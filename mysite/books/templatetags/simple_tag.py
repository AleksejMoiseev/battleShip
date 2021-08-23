from django import template
register = template.Library()


@register.simple_tag
def check_is_five(*args):
    list_perms = list(args)
    print('value', list_perms)
    return True
