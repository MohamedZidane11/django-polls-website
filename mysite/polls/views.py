from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-publish_date')[:5]
    context = {'latest_questions' : latest_questions}
    return render(request, 'polls/index.html', context)
    # return HttpResponse("awesome job guys, this is the index page, of our polls app")


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id )
    context = {'question' : question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse(f"this is the result of the question: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"votes on question: {question_id}")
