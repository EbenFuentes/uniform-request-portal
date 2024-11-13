from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("Hello, you are in the uniform_req_app home_view.")
