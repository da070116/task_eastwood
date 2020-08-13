from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name="list"),
    path('actual/', views.EmployeesRecentView.as_view(), name="actual"),
    path('dict/', views.EmployeeDictionaryView.as_view(), name="dict"),
    path('dict/<int:part>', views.EmployeeDictionaryView.as_view(), name="dict_part"),
    path('dept/<int:dept>', views.EmployeesDeptView.as_view(), name="dept"),
    path('<int:pk>', views.EmployeeDetail.as_view(), name="detail"),
]
