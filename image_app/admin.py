from django.contrib import admin
from .models import *

admin.site.site_header = "Image Gallery"
admin.site.site_title = "Image Gallery Admin Portal"
admin.site.index_title = "Welcome to Image Gallery Portal"



@admin.register(Batch1)
class Batch1Admin(admin.ModelAdmin):
    pass

@admin.register(Batch2)
class Batch1Admin(admin.ModelAdmin):
    pass

@admin.register(Batch3)
class Batch1Admin(admin.ModelAdmin):
    pass

@admin.register(Batch4)
class Batch1Admin(admin.ModelAdmin):
    pass

@admin.register(Batch5)
class Batch1Admin(admin.ModelAdmin):
    pass



