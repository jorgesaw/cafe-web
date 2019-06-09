from .models import Link

def ctx_dict(reuqest):
    ctx = {}
    links = Link.objects.filter(active=True)
    for link in links:
        ctx[link.key] = link.url
    return ctx