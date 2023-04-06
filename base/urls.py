from django.urls import path
from django.urls import path
from django.contrib.auth import views as auth_views
from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user_register/', views.user_register, name="register"),
    path('user_login/', views.user_login, name="login"),
    path('user_logout/', views.user_logout, name="logout"),

    path('user_profile/<str:pk>', views.user_profile, name="user-profile"),
    path('user_update/<str:pk>', views.user_update, name="user-update"),

    path('event_page/<str:pk>', views.event_page, name="event-page"),

    path('event_registration/<str:pk>', views.event_registration, name="event-registration"),
    path('event_submission/<str:pk>', views.event_submission, name="event-submission"),
    path('update_submission/<str:pk>', views.update_submission, name="update-submission"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
