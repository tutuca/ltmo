from rest_framework import serializers
from .models import Leak


class LeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leak
