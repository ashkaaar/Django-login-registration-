from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
]