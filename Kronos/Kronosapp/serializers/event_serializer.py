from rest_framework import serializers
from ..models import Event, EventType
from django.utils import timezone


class EventSerializer(serializers.ModelSerializer):
    startDate = serializers.DateTimeField(input_formats=['%d/%m/%Y'])
    endDate = serializers.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Event
        fields = '__all__'

    def validate_startDate(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de inicio no puede ser anterior a la fecha actual.")
        return value

    def validate_endDate(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de fin no puede ser anterior a la fecha actual.")
        return value

    def validate(self, data):
        if data['startDate'] > data['endDate']:
            raise serializers.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        return data

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'