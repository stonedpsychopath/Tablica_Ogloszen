from django.contrib import admin

from .models import Comments, Categories, Announcement, CustomUser

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','likes']
    list_filter = ('name','likes')
    search_fields = ('name','likes')

    def get_name(self, obj):
        return obj.name.name_text

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ('name',)
    search_fields = ('name',)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['description','get_category','price','name']
    list_filter = ['description','price','name']
    search_fields = ('description','price','name')

    def get_category(self,obj):
        return obj.categories.name


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','email','is_staff','is_active','is_superuser']
    list_filter = ('first_name','last_name','username','email','is_staff','is_active','is_superuser')
    search_fields = ('first_name','last_name','username','email','is_staff','is_active','is_superuser')


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(CustomUser,UserAdmin)