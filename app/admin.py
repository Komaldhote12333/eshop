from django.contrib import admin
from .models import *



class tabularimage(admin.TabularInline):
    model = images
# Register your models here.
class tabulartage(admin.TabularInline):
    model = Tag
    
class tabularimage(admin.ModelAdmin):
    inlines =[tabularimage,tabulartage]
    
admin.site.register(Brand)    
admin.site.register(Product,tabularimage)    

admin.site.register(images)    

admin.site.register(Category)    

admin.site.register(Tag)    

admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Contact)
admin.site.register(Orderform)
admin.site.register(Team)


    