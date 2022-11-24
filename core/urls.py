from django.urls import path
from .views import *

urlpatterns = [
    path('kolaaa/', kolaa),
    path('pepsiii/', pepsii),
    path('flashhh/', flashh),
    path('ferrariii/', ferrarii),
]