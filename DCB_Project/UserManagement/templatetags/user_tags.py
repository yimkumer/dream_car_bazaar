from django import template

register = template.Library()


@register.filter(name='user_groups')
def user_groups(user):
    group_list = user.groups.values_list('name', flat=True)
    return list(group_list)
