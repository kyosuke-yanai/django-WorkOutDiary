from django import forms
from .models import WorkOutRecord, WorkOutMenu

class WorkOutRecordForm(forms.ModelForm):
    class Meta:
        model = WorkOutRecord
        fields = '__all__'
        exclude = ('sets',)

class WorkOutDetailRecordForm(forms.Form):
    pass

class WorkOutMenuForm(forms.ModelForm):
    class Meta:
        model = WorkOutMenu
        fields = '__all__'