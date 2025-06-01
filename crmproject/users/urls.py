from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/customer/', views.dashboard_view, name='dashboard'),
    # path('dashboard/normal/', views.normal_dashboard, name='normal_dashboard'),
    path('profile/edit',views.edit_profile_view, name='edit_profile'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('passwordchange/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='passwordchange_done'),
    path('orders/', views.view_orders, name='view_orders'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/update/<int:order_id>/', views.update_order, name='update_order'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('orders/status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('orders/all/', views.all_orders_view, name='all_orders'),



]
