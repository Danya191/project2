from django.urls import path
from authentication.views import simple_view


urlpatterns = [
    path('', simple_view)
]