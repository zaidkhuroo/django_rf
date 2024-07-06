from . import models
from rest_framework import serializers

class Testserializer(serializers.ModelSerializer):
    def get(self, request):
        class Meta:
            model = models.Post
            fields = {
                'title','description'
            }
              