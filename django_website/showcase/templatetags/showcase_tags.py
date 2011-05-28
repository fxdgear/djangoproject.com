from django import template

from ..models import Website, DjangoFeature

register = template.Library()

@register.inclusion_tag('showcase/websites.html')
def render_websites(num):
    websites = Website.objects.all()[:num]
    return {
        'websites': websites,
    }

@register.inclusion_tag('showcase/django_features.html')
def render_django_features(num):
    features = DjangoFeature.objects.all()[:num]
    return {
        'features': features,
    }
