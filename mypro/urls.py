from django.contrib import admin
from django.urls import path, include  # ✅ Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # ✅ Include app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Django Auth URLs
]
