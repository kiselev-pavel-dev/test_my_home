from rest_framework import serializers

from entity.models import Entity


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Entity
        fields = ("value", "properties")

    def get_properties(self, obj):
        return {item.key: item.value for item in obj.properties.all()}
