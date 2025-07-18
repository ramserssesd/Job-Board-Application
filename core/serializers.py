from rest_framework import serializers
from .models import Job, Application, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    resume = serializers.FileField()

    class Meta:
        model = Application
        fields = '__all__'
