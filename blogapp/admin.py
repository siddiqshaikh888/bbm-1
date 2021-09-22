from django.contrib import admin
from .models import BlogModel, CommentModel, Category
admin.site.register(BlogModel)
admin.site.register(Category)
admin.site.register(CommentModel)
# Register your models here.
#class CommentAdmin(admin.ModelAdmin):
 #   list_display = ('your_name', 'approved')  


