from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
      path('', views.sql_editor, name='sql_editor'),
    path('sql-tables/', views.sql_tables_view, name='sql_tables'),
        path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
     path('help/', views.help_page, name='help_page'),  # Add this line
]


