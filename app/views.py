from email.policy import default
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import WorkOutRecord, WorkOutRepsRecord
from django.urls import reverse, reverse_lazy
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
            WorkOutRepsRecord.objects.create(menu=WorkOutRecord.objects.all().last(), reps=0, weight=0)
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

class WorlOutDiaryRecordDetailView(FormView):
    template_name = 'app/workout_diary_record_detail.html'
    form_class = WorkOutRecordRepsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reps_forms = WorkOutRecordRepsForm()
        for index in range(int(WorkOutRecord.objects.get(pk=self.kwargs['pk']).sets)):
            reps_forms.fields[index] = forms.CharField(label=str(index))
        context['reps_forms'] = reps_forms
        context['workoutrecord'] = WorkOutRecord.objects.get(pk=self.kwargs['pk'])
        context['workoutrepsrecords'] = WorkOutRepsRecord.objects.filter(menu=WorkOutRecord.objects.get(pk=self.kwargs['pk']))
        return context

    def get_post_form(self, index, reps):
        if self.request.POST.get(index) == None:
            return reps
        return int(self.request.POST.get(index))

    def form_valid(self, form):
        form = super().form_valid(form)
        for index in range(int(WorkOutRecord.objects.get(pk=self.kwargs['pk']).sets)):
            workoutrepsrecord_date = WorkOutRepsRecord.objects.filter(menu=WorkOutRecord.objects.get(pk=self.kwargs['pk']))[index]
            workoutrepsrecord_date.reps = self.get_post_form(str(index), workoutrepsrecord_date.reps)
            workoutrepsrecord_date.save()
        return form

    def get_success_url(self):
        return reverse('workout_diary_record_detail', kwargs={'year': self.kwargs['year'], 'month': self.kwargs['month'], 'day': self.kwargs['day'], 'pk': self.kwargs['pk']})