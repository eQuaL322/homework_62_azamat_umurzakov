from django.contrib import admin

from issue_tracker.models import Task, Type, Status, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'summary', 'status', 'types', 'created_at')
    search_fields = ('summary', 'description')
    fields = ('summary', 'description', 'status', 'types', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('summary',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at')
    search_fields = ('name',)
    fields = ('name', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('name',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at')
    search_fields = ('name',)
    fields = ('name', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_date', 'end_date']
    list_filter = ['id', 'name', 'description', 'start_date', 'end_date']
    search_fields = ['id', 'name']
    fields = ['name', 'description', 'start_date', 'end_date', 'users']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
