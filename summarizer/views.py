from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .models import SummaryTask
from .tasks import summarize_text
import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if not text:
            return render(request, 'summarizer/index.html', {'error': 'Please paste some text first.'})
        
        task = SummaryTask.objects.create(original_text=text)
        summarize_text.delay(str(task.id))
        return redirect('task_detail', task_id=str(task.id))

    tasks = SummaryTask.objects.all().order_by('-created_at')
    return render(request, 'summarizer/index.html', {'tasks': tasks})


def task_detail(request, task_id):
    try:
        task = SummaryTask.objects.get(id=task_id)
    except SummaryTask.DoesNotExist:
        return render(request, 'summarizer/task_detail.html', {'error': 'Task not found'})
    return render(request, 'summarizer/task_detail.html', {'task': task})


@method_decorator(csrf_exempt, name='dispatch')
class SubmitTaskView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            text = request.data.get('text', '').strip()
            if not text:
                return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)
            task = SummaryTask.objects.create(original_text=text)
            summarize_text.delay(str(task.id))
            return Response({'task_id': str(task.id)}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error in SubmitTaskView: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskStatusView(APIView):
    def get(self, request, task_id):
        try:
            task = SummaryTask.objects.get(id=task_id)
        except SummaryTask.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'task_id': str(task.id),
            'status': task.status,
            'summary': task.summary,
            'error_message': task.error_message,
            'created_at': task.created_at.strftime('%d %b %Y, %H:%M'),
            'completed_at': task.completed_at.strftime('%d %b %Y, %H:%M') if task.completed_at else None,
        })


class AllTasksView(APIView):
    def get(self, request):
        try:
            tasks = SummaryTask.objects.all().order_by('-created_at')
            data = []
            for task in tasks:
                data.append({
                    'task_id': str(task.id),
                    'text_preview': task.original_text[:80] + '...' if len(task.original_text) > 80 else task.original_text,
                    'status': task.status,
                    'created_at': task.created_at.strftime('%d %b %Y, %H:%M'),
                })
            return Response({'tasks': data})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)