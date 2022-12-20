from django.contrib import admin

from .models import Comments, Categories, Announcement, CustomUser

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','likes','get_announcement']
    list_filter = ('name','likes')
    search_fields = ('name','likes')
    raw_id_fields = ('announcement',)

    def get_announcement(self, obj):
        return obj.announcement.name

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ('name',)
    search_fields = ('name',)

    def get_announcement(self, obj):
        return obj.announcement.name

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['get_category','price','name','description']
    list_filter = ['description','price','name']
    search_fields = ('description','price','name')
    raw_id_fields = ('categories',)

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