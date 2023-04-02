from django.urls import path
from django.urls import path

from base import views

urlpatterns = [
    path('',views.home , name="home" ),
    path('user_register/', views.user_register, name="register"),
    path('user_login/', views.user_login, name="login"),
    path('user_logout/', views.user_logout, name="logout"),

    path('user_profile/', views.user_profile, name="user-profile"),

    path('event_page/<str:pk>', views.event_page, name="event-page"),

    path('event_registration/<str:pk>', views.event_registration, name="event-registration"),
    path('event_submission/<str:pk>', views.event_submission, name="event-submission"),
    path('update_submission/<str:pk>', views.update_submission, name="update-submission"),
]