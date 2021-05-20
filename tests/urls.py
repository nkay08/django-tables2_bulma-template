from django.urls import path
from django.views.generic import View

from tests.views import TableView

urlpatterns = [
    path("simple/action/", View.as_view(), name="simpleAction"),
    path("", TableView.as_view(), name="index"),
]