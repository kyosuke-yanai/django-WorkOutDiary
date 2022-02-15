from django.urls import path
from . import views

urlpatterns = [
    path('workout-diary/<int:pk>', views.Test.as_view(), name='test'),
    path('', views.WorkOutDiaryListView.as_view(), name='workout_diary_list'),
    path('workout-diary/record', views.WorkOutDiaryRecordView.as_view(), name='workout_diary_record'),   
    path('workout-diary/record/<int:year>/<int:month>/<int:day>', views.WorkOutDiaryRecordListView.as_view(), name='workout_diary_record_list'),
    path('workout-diary/record/<int:year>/<int:month>/<int:day>/detail/<int:pk>', views.WorlOutDiaryRecordDetailView.as_view(), name='workout_diary_record_detail'),   
    path('workout-diary/menu', views.WorkOutMenuListView.as_view(), name='workout_menu_list'),   
    path('workout-diary/menu/<int:pk>', views.WorkOutMenuDetailView.as_view(), name='workout_menu_detail'),   
]