from django import forms
from .models import WorkOutRecord, WorkOutRepsRecord

class WorkOutRecordForm(forms.ModelForm):
    class Meta:
        model = WorkOutRecord
        fields = '__all__'

class WorkOutRecordRepsForm(forms.Form):
    pass