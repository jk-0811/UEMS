from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('contact/', views.contact, name='contact'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('registration/', views.registration, name='registration'), 
    path('submit-registration/', views.submit_registration, name='submit_registration'),
    path('conference/', views.conference, name='conference'),
    path('ai/', views.ai_workshop, name='ai_workshop'),
    path('chatbot/', views.chatbot_workshop, name='chatbot_workshop'),
    path('events/', views.events, name='events'),

    # Use Django's LoginView with custom template
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),

    # You can still include auth URLs if needed (password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
