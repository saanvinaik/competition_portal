from django.contrib import admin
from .models import Category , Branch, Competition, CompetitionAttribute, Domain , Year, slider

admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(slider)
admin.site.register(CompetitionAttribute)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id','title','branch','year' ,'domain','reg_fee','status')
    list_editable = ('status' , )
admin.site.register(Competition , CompetitionAdmin)

# Register your models here.
