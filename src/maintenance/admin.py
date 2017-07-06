from django.contrib import admin

from .models import Worker


class WorkerInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = 'Worker'
    fk_name = 'user'
