# pages/context_processors.py
from .models import Page

def page_tree(request):
    return {
        'pages': Page.objects.filter(parent=None, published=True)
    }