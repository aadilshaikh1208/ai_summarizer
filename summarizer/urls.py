from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/submit/', views.SubmitTaskView.as_view(), name='submit_task'),
    path('api/status/<str:task_id>/', views.TaskStatusView.as_view(), name='task_status'),
    path('api/tasks/', views.AllTasksView.as_view(), name='all_tasks'),
    path('task/<str:task_id>/', views.task_detail, name='task_detail'),  
]