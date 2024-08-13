from rest_framework import serializers
from ..models import Year
from .preceptor_serializer import PreceptorSerializer

class YearSerializer(serializers.ModelSerializer):
    preceptors=PreceptorSerializer(many=True, read_only=True)
    class Meta:
        model = Year
        fields = ['id','name', 'description', 'number']

    def validate_number(self, value):
        request = self.context.get('request')
        years_number= Year.objects.filter(school=request.school).values_list('number', flat=True)
        if str(value) in years_number:
            raise serializers.ValidationError('Ya existe un año con ese número')
        return value
