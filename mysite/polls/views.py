from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("awesome job guys, this is the index page, of our polls app")


def detail(request, question_id):
    return HttpResponse(f"this is the detail view of the question: {question_id}")


def results(request, question_id):
    return HttpResponse(f"this is the result of the question: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"votes on question: {question_id}")
