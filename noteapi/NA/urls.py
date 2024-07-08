from django.urls import path
from .views import *
from . import views
from .rest_views import NoteList, NoteDetail

urlpatterns = [
    # Normal views
    path('', views.note_list, name='note_list'),
    path('notes/create/', note_create, name='note_create'),
    path('notes/<slug:slug>/', note_detail, name='note_detail'),
    path('notes/<slug:slug>/edit/', note_update, name='note_update'),
    path('notes/<slug:slug>/delete/', note_delete, name='note_delete'),

    path('folders/', folder_list, name='folder_list'),
    path('folders/create/', folder_create, name='folder_create'),
    path('folders/<slug:slug>/', folder_detail, name='folder_detail'),
    path('folders/<slug:slug>/edit/', folder_update, name='folder_update'),
    path('folders/<slug:slug>/delete/', folder_delete, name='folder_delete'),

    # API views
    path('api/notes/', NoteList.as_view(), name='api_note_list'),
    path('api/notes/<slug:slug>/', NoteDetail.as_view(), name='api_note_detail'),
]
