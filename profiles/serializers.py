from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        reuqest = self.context.get('request')
        return reuqest.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'created_at', 'updated_at',
            'content', 'image', 'is_owner'
        ]