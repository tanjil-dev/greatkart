from django.contrib import admin
from .models import Category, SubCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_staff
    list_display = ('category_name', 'slug', 'description')
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_staff
    list_display = ('subcategory_name', 'category', 'slug', 'description')
    prepopulated_fields = {'slug': ('subcategory_name',)}
    list_filter = ('category',)
