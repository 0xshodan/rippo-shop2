from django.urls import path

from .views import FeedbacksView

urlpatterns = [path("", FeedbacksView.as_view())]
