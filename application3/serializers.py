from rest_framework import *
from application3.models import *


class FacebookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Facebook
		fields = ("First_name","Last_name","Password", "Re_password", "Phone_no","Email_id" )