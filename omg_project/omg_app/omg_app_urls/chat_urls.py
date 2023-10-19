from django.urls import path
from ..omg_app_views import chat_views

urlpatterns = [
    path('messages/<int:chat_id>/', chat_views.messages, name='messages'),
]