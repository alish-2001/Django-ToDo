from django.contrib import admin

from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

  list_display=['user','title','description','is_done','deadline_datetime','datetime_created','datetime_modified', ]
  


  