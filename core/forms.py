from django import forms
from .models import ModelUploadFile

class FormUploadFile(forms.ModelForm):
    class Meta:
        model = ModelUploadFile
        fields = '__all__'
