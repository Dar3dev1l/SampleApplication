from django.urls import path, include
from .views import SportListView, SportDetailView

urlpatterns = [
    path('', SportListView.as_view()),
    path('<pk>', SportDetailView.as_view())
]
