from django.urls import path, include


urlpatterns = [
    path('', include('sql_editor.urls')),
]
