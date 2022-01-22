from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from jquery.models import Username


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        fields = '__all__'