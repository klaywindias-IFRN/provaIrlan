from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Atleta

def index(request):
    latest_question_list = Atleta.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

