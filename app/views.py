from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import WorkOutRecord, WorkOutRepsRecord
from django.urls import reverse_lazy
from .forms import WorkOutRecordForm, WorkOutRecordRepsForm
from django import forms

class Test(ListView):
    template_name = 'app/test.html'
    model = WorkOutRecord

class WorkOutDiaryListView(ListView):
    template_name = 'app/workout_diary_list.html'

    def get_queryset(self):
        return WorkOutRecord.objects.distinct().values_list('record_date').order_by('-record_date')

class WorkOutDiaryRecordView(CreateView):
    template_name = 'app/workout_diary_record.html'
    model = WorkOutRecord
    form_class = WorkOutRecordForm
    success_url = reverse_lazy('workout_diary_list')

    def form_valid(self, form):
        form = super().form_valid(form)
        for _ in range(int(self.request.POST.get('sets'))):
            WorkOutRepsRecord.objects.create(menu=WorkOutRecord.objects.all().last())
        return form

class WorkOutDiaryRecordListView(ListView):
    template_name = 'app/workout_diary_record_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        context['month'] = self.kwargs['month']
        context['day'] = self.kwargs['day']
        return context

    def get_queryset(self):
        return WorkOutRecord.objects.filter(record_date__year=self.kwargs['year'], record_date__month=self.kwargs['month'], record_date__day=self.kwargs['day'])

class EmptyClass(forms.Form):
    pass

class WorlOutDiaryRecordDetailView(FormView):
    template_name = 'app/workout_diary_record_detail.html'
    form_class = WorkOutRecordRepsForm
    success_url = reverse_lazy('workout_diary_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reps_forms = EmptyClass()
        for index in range(int(WorkOutRecord.objects.get(pk=self.kwargs['pk']).sets)):
            reps_forms.fields[index] = forms.CharField(label=str(index))
        context['reps_forms'] = reps_forms
        context['workoutrecord'] = WorkOutRecord.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        WorkOutRepsRecord.objects.create(menu=WorkOutRecord.objects.get(pk=self.kwargs['pk']), reps=form.data.get("reps"))
        return super().form_valid(form)