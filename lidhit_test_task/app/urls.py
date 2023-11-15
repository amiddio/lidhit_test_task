from django.urls import path
from .views import FormCheckerView

app_name = 'app'

urlpatterns = [
    path('get_form', FormCheckerView.as_view(), name='get_form'),
]
