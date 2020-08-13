from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('eastwood.core.urls')),
    path('employees/', include('eastwood.employees.urls')),
    path('admin/', admin.site.urls),
]
