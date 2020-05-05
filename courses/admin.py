from django.contrib import admin
from .models import Content, Course, Module, Subject
from django.contrib import admin

# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

#@admin.register(Content)
class ContentInline(admin.StackedInline):
    model = Content

#@admin.register(Module)
class ModuleInline(admin.StackedInline):
    model = Module
    #inlines = [ContentInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

