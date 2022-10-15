from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration Page</h1>")

def Home(request):
    # return HttpResponse("<h1>Welcome to the Prime Intuit Registration Home Page</h1>")
    # my_dict = {'Insert_Me': "I am a text from Registration/Views.py from subtemplate"}
    # batch_list = Batch.objects.order_by('batch_ID')
    # batch_list = Batch.objects.raw('select * from Registration_batch where start_date > "2022-06-01"')
    batch_list = Batch.objects.raw('select * from Registration_batch')
    data_dict = {'access_record': batch_list,'Insert_Me': "I am a text from Registration/Views.py"}
    return render(request, 'Registration/index.html', context = data_dict)