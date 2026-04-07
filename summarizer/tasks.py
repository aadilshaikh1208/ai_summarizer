from celery import shared_task
from django.utils import timezone
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from .models import SummaryTask
import os

@shared_task
def summarize_text(task_id):

    task = SummaryTask.objects.get(id=task_id)
    task.status = 'processing'
    task.save()

    try:
        llm = init_chat_model(
            model="llama-3.1-8b-instant",
            model_provider="groq",
            temperature=0.3,
            groq_api_key=os.getenv('GROQ_API_KEY')
        )

        prompt = f"Please summarize the following text in a clear and concise way:\n\n{task.original_text}"
        response = llm.invoke([HumanMessage(content=prompt)])

        task.summary = response.content
        task.status = 'completed'
        task.completed_at = timezone.now()
        task.save()

    except Exception as e:
        task.status = 'failed'
        task.error_message = str(e)
        task.save()