# forms.py 
# from django import forms
from rest_framework import serializers
from .models import imageProcess


class ImageProcessSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = imageProcess
        fields = ['image_upload', 'image_url']

    def get_image_url(self, obj):
        return obj.image_upload.url
