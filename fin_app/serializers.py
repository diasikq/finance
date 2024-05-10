from rest_framework import serializers
from .models import FinancialOrganization


class FinancialOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOrganization
        fields = '__all__'  # Сериализовать все поля модели
