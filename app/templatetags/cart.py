from django import template


register = template.Library()

@register.filter(name ="is_in_cart")
def is_in_cart(p,q):
    v = 0
    v= int(p) *int(q) 
    return v


@register.filter(name ="total")
def total(value):
    
        return value
    

