# from . import models
from . models  import Post
from rest_framework import serializers

class TestSerializer(serializers.ModelSerializer):
    class Meta:
            model = Post
            fields = [
                'title','description','owner'
            ]
              