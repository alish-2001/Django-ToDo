from django.urls import path 

from .import views

app_name='todo'

urlpatterns = [
    path('',views.TaskListView.as_view(),name='task_list'),
    path('<int:pk>/',views.TaskDetailView.as_view(),name='task_detail'),
    path('add/',views.TaskCreateView.as_view(),name='add_task'),
    path('edit/<int:pk>',views.TaskUpdateView.as_view(),name='edit_task'),
    path('delete/<int:pk>',views.TaskDeleteView.as_view(),name='delete_task'),
    path('<int:id>/done',views.task_done,name='task_done'),
    path('notify/',views.task_notify,name='notify'),
]
