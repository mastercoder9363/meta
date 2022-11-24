from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kolaaa/', include('core.urls')),
    path('pepsiii/', include('core.urls')),
    path('flashhh/', include('core.urls')),
    path('ferrariii/', include('core.urls')),
]
