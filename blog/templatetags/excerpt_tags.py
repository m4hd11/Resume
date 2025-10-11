from django import template

register = template.Library()

@register.filter(name='excerpt')
def excerpt(value, num_words=30):

    if not isinstance(value, str):
        value = str(value)

    words = value.split()
    if len(words) <= num_words:
        return value
    return " ".join(words[:num_words]) + "..."
