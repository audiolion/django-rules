from django import template

from ..rulesets import default_rules


register = template.Library()


@register.assignment_tag
def test_rule(name, obj=None, target=None):
    return default_rules.test_rule(name, obj, target)


@register.assignment_tag
def has_perm(perm, user, obj=None):
    if not hasattr(user, 'has_perm'):
        return False  # swapped user model that doesn't support permissions
    else:
        return user.has_perm(perm, obj)
