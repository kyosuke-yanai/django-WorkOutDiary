from django import forms
from .models import WorkOutRecord

class WorkOutRecordForm(forms.ModelForm):
    class Meta:
        model = WorkOutRecord
        fields = '__all__'

class WorkOutDetailRecordForm(forms.Form):
    pass