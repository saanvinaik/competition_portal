from django.contrib import admin
from .models import Category , Branch, Competition, CompetitionAttribute, Domain , Year, slider

admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(slider)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id','title','branch','year' ,'domain','status')
    list_editable = ('status' , )
admin.site.register(Competition , CompetitionAdmin)

# Register your models here.

class CompetitionAttributeAdmin(admin.ModelAdmin):
        list_display = ('id','competition','reg_fee','domain','year')
admin.site.register(CompetitionAttribute,CompetitionAttributeAdmin)

