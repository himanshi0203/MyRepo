from rest_framework import serializers
from .models import CompanyDetails

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails