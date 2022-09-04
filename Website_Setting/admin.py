from django.contrib import admin
from Website_Setting.models import Homepage_animated_line, website_logo
from django.utils.html import format_html

class Homepage_animated_lineAdmin(admin.ModelAdmin):
    list_display = ('Animated_line','action')
    list_display_links= None
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/Website_Setting/homepage_animated_line/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None) :
        return False
admin.site.register(Homepage_animated_line, Homepage_animated_lineAdmin)

class website_logoAdmin(admin.ModelAdmin):
    list_display = ('logo','logo_preview','action')
    list_display_links= None
    def logo_preview(self, obj):
        return format_html(f'<img src= "/media/{obj.logo}"style ="width:100px; height:auto; background:black"')
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/Website_Setting/website_logo/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')
    def has_delete_permission(self, request, obj=None) :
        return False
    def has_add_permission(self, request):
        return False
admin.site.register(website_logo, website_logoAdmin)


