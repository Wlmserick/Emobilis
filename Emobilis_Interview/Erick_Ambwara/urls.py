from django.urls import path
from .views import CreateStudent,GetStudent

urlpatterns = [
    path('', CreateStudent, name='create_student'),
    path('std_detail/<str:reg>/', GetStudent, name='std_detail'),
    #path('delete/<int:id>', Delete, name='delete'),
]