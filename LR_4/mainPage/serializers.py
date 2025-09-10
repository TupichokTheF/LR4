from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User

from .models import Incidents, CyberAttack, SourceIncident, StatusIncidents

class AttacksSerializer(serializers.ModelSerializer):

    #Author = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())
    Author = serializers.HiddenField(default = CurrentUserDefault())
    Attack = serializers.SlugRelatedField(slug_field='attack_name', queryset=CyberAttack.objects.all())
    Status = serializers.SlugRelatedField(slug_field='status', queryset=StatusIncidents.objects.all())
    Source = serializers.SlugRelatedField(slug_field='source', queryset=SourceIncident.objects.all())

    class Meta:
        model = Incidents
        fields = '__all__'

class UpdateAttack(serializers.ModelSerializer):

    Author = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())
    Attack = serializers.SlugRelatedField(slug_field='attack_name', queryset=CyberAttack.objects.all())
    Status = serializers.SlugRelatedField(slug_field='status', queryset=StatusIncidents.objects.all())
    Source = serializers.SlugRelatedField(slug_field='source', queryset=SourceIncident.objects.all())

    class Meta:
        model = Incidents
        fields = '__all__'