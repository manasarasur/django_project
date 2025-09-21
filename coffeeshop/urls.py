from django.contrib import admin
from django.urls import path, include
from coffee.views import home  # optional home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffee/', include('coffee.urls')),  # your app URLs
    path('', home),  # optional root URL so visiting / works
]
