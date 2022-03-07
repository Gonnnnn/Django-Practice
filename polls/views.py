import datetime
from django.utils import timezone
from django.http import Http404, HttpResponse
from django.shortcuts import render

from polls.models import Question
from .serializers import QuestionSerializer
from rest_framework.renderers import JSONRenderer
import io

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    print(latest_questions[0])
    output = ', '.join([q.question_text for q in latest_questions])
    return HttpResponse(output)


def get(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(question.question_text)

def test(request):
    # temp = {"question_text":"TEST2"}
    # serializer = QuestionSerializer(data=temp)
    # if serializer.is_valid():
    #     print(type(serializer.validated_data))
    #     print(serializer.validated_data)
    print(type(request.data))
    return HttpResponse()