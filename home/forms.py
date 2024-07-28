from django.forms import ModelForm
from .models import *

class SampleModelForm(ModelForm):
    class Meta:
        model = SampleModel
        fields = '__all__'