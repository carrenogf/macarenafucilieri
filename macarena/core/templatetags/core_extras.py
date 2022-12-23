from datetime import datetime
from django import template
from core.models import footer
import datetime
register = template.Library()

@register.simple_tag
def get_footer():
    if footer.objects.filter(selecionado=True).exists():
        footer_selected = footer.objects.get(selecionado=True)
        return footer_selected
    else:
        return None