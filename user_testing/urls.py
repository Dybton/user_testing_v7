from django.contrib import admin
from django.urls import path, include
from content import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls')),
]
