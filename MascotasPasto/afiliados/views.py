from django.shortcuts import render

# Create your views here.
def index(request):
 return HttpResponse('Welcome,this is our first')