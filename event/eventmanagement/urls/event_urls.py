from django.urls import path
from eventmanagement import views

urlpatterns = [
    path('v1/events/', views.get_events),
    path('v1/events/create/', views.create_event),
    path('v1/events/<int:event_id>/', views.event_detail),
    path('v1/registrations/', views.registration_list),
]