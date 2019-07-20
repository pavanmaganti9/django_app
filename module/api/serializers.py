from rest_framework import serializers
from .models import Songs


class SongsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Songs
		fields = ('id',"title", "artist")
	
	
	def validate_title(self, value):
		qs = Songs.objects.filter(title__iexact=value)
		if self.instance:
			qs = qs.exclude(id=self.instance.id)
		if qs.exists():
			raise serializers.ValidationError("Title must be unique")
		return value