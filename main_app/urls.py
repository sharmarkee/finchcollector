from django.urls import path
from . import views
	
urlpatterns = [
	 path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('finches/', views.finches_index, name='index'),
   path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
   path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
   path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
   path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
   path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
   path('finch/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
   path('finch/<int:finch_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
   path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
   path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
 ]