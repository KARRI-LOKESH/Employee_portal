from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login_view, name='login'),
    path('add/', views.employee_add, name='employee_add'),
    path('search/', views.employee_search, name='employee_search'),
    path('view/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('bulk-delete/', views.employee_bulk_delete, name='employee_bulk_delete'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('logout/', views.logout_view, name='logout'),
    path('history/<int:pk>/', views.employee_history, name='employee_history'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)