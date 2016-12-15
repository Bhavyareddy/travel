from django.shortcuts import render
from django.http import HttpResponse
from application3.models import Facebook
from application3.serializers import FacebookSerializer
from rest_framework.response import Response



def  passenger_facebook(request):
    return render(request,'facebook.html')
def passenger_login(request):
	return render(request,'login.html')

# Create your views here.
