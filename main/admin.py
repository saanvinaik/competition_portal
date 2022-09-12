from django.contrib import admin
from .models import Category , Branch, Competition, CompetitionAttribute, Domain , Year, slider

admin.site.register(slider)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Domain)
# admin.site.register(Competition)
# admin.site.register(CompetitionAttribute)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id','title','branch','year' ,'domain','status')
    list_editable = ('status' , )
admin.site.register(Competition , CompetitionAdmin)

# Register your models here.

class CompetitionAttributeAdmin(admin.ModelAdmin):
        list_display = ('id','competition','reg_fee','domain','year')
admin.site.register(CompetitionAttribute,CompetitionAttributeAdmin)

