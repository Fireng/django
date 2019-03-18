from django.http import HttpResponse

# Create your views here.

def index(request, question_id):
    return HttpResponse("hi %s." % question_id)

