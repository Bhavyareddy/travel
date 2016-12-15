from rest_framework import *
from application.models import *


class LoginSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Login
		fields = ("First_Name", "Last_Name","Email_id","Phone_no","Address")