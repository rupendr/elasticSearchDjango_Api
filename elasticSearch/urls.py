from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index.html'),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
    path('CsvFileUpload/', views.CsvFileUpload.as_view())

]
