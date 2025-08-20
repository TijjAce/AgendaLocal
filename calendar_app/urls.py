from django.urls import path
from . import views
from . import analytics_views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('get-events/', views.get_events, name='get_events'),
    path('daily-schedule/<int:year>/<int:month>/<int:day>/', views.daily_schedule_canvas, name='daily_schedule'),
    path('weekly-schedule/', views.weekly_schedule, name='weekly_schedule'),
    path('weekly-schedule/<int:year>/<int:week>/', views.weekly_schedule, name='weekly_schedule_with_params'),
    path('toggle-completion/<int:session_id>/', views.toggle_session_completion, name='toggle_session_completion'),


    path("update-session-date/", views.update_session_date, name="update_session_date"),
    
    path('update-session-position/', views.update_session_position, name='update_session_position'),
    
    
    
    # Analytics URLs
    path('Analyse/', analytics_views.radar_analytics, name='radar_analytics'),
    path('api/competencies-radar/', analytics_views.competencies_radar_api, name='competencies_radar_api'),
    path('api/fiches-radar/', analytics_views.fiches_radar_api, name='fiches_radar_api'),
    path('api/hours-radar/', analytics_views.hours_radar_api, name='hours_radar_api'),
    path('api/discipline-competencies-radar/', analytics_views.discipline_competencies_radar_api, name='discipline_competencies_radar_api'),
]
