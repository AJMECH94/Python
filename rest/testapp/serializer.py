from rest_framework.serializers import ModelSerializer
from .models import Emp

class Empserializer(ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'
