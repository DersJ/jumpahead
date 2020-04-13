from django.urls import path
from . import views

urlpatterns = [
	path('', views.moduleList, name='moduleList'),
    path('<int:pk>/', views.ModuleDetailView.as_view(), name='moduleDetail'),
]