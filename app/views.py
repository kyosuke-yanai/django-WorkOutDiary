from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView, DetailView
from .models import WorkOutRecord, WorkOutRepsRecord, WorkOutMenu
from django.urls import reverse, reverse_lazy
from .forms import WorkOutRecordForm, WorkOutDetailRecordForm
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
        menu_data = WorkOutMenu.objects.get(pk=self.request.POST.get('menu'))
        for _ in range(int(menu_data.sets)):
            WorkOutRepsRecord.objects.create(menu=WorkOutRecord.objects.all().last(), reps=menu_data.reps, weight=menu_data.weight)
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
    form_class = WorkOutDetailRecordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reps_forms = WorkOutDetailRecordForm()
        weight_forms = WorkOutDetailRecordForm()
        workoutrecord_data = WorkOutRecord.objects.get(pk=self.kwargs['pk'])
        for index in range(workoutrecord_data.menu.sets):
            reps_forms.fields[index] = forms.IntegerField(label=str(index), initial=WorkOutRepsRecord.objects.filter(menu=workoutrecord_data)[index].reps)
            weight_forms.fields[index] = forms.IntegerField(label=str(index), initial=WorkOutRepsRecord.objects.filter(menu=workoutrecord_data)[index].weight)
        context['reps_forms'] = reps_forms
        context['weight_forms'] = weight_forms
        context['workoutrecord'] = workoutrecord_data
        return context

    def get_post_form(self, index, reps, weight):
        if self.request.POST.getlist(index) == []:
            return (reps,weight)
        return self.request.POST.getlist(index)

    def form_valid(self, form):
        form = super().form_valid(form)
        for index, workoutrepsrecord_date in enumerate(WorkOutRepsRecord.objects.filter(menu=WorkOutRecord.objects.get(pk=self.kwargs['pk']))):
            workoutrepsrecord_detail_date = self.get_post_form(str(index), workoutrepsrecord_date.reps, workoutrepsrecord_date.weight)
            workoutrepsrecord_date.reps = int(workoutrepsrecord_detail_date[0])
            workoutrepsrecord_date.weight = int(workoutrepsrecord_detail_date[1])
            workoutrepsrecord_date.save()
        return form

    def get_success_url(self):
        return reverse('workout_diary_record_detail', kwargs={'year': self.kwargs['year'], 'month': self.kwargs['month'], 'day': self.kwargs['day'], 'pk': self.kwargs['pk']})

class WorkOutMenuListView(ListView):
    template_name = 'app/workout_menu_list.html'
    model = WorkOutMenu

class WorkOutMenuDetailView(DetailView):
    template_name = 'app/workout_menu_detail.html'
    model = WorkOutMenu