from rest_framework import serializers
from Gym.models import Sport, Area, Equipment


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "area", "available"]


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ["id", "equipment", "available"]


class SportSerializer(serializers.ModelSerializer):
    area = serializers.StringRelatedField(many=True)
    equipment = serializers.StringRelatedField(many=True)

    class Meta:
        model = Sport
        fields = ["area", "equipment", "sport_name", "max_players", "min_players", "team_sport"]