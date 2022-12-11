# forms.py
from django import forms
#from rest_framework import serializers
from .models import imageProcess


class ImageForm(forms.ModelForm):

    class Meta:
        model = imageProcess
        fields = ['image_upload']
