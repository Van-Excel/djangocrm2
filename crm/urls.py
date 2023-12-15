from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('signup/', views.signup, name='signup'),
    path('add/', views.new_record, name='new_record'),
    path('record/<int:pk>', views.customer_record, name='customer_record'),
    path('update/<int:pk>', views.update_record, name='update_record'),
    path('delete/<int:pk>', views.delete_record, name = 'delete_record' ),
]
