from django.shortcuts import render
from rest_framework import status,permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from application.models import Login
from application.serializers import LoginSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def passenger_login(request):
	if request.method == 'GET':
		passenger = Login.objects.all()
		serializer =LOginSerializer(passenger, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = LoginSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
