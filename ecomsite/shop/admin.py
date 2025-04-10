from django.contrib import admin
from .models import Product,Order

admin.site.site_header = "Ecomsite Admin"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Welcome to ABC Shopping"



# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','discount_price','category','description']
    search_fields = ['title','category','price']



    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Change category to default'
    actions = ('change_category_to_default',)
    fields =( 'title','price',)
    list_editable = ('price',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
