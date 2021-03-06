from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/pendingactions/", views.agent_pending_actions),
    path("allpendingactions/", views.all_pending_actions),
    path("cancelpendingaction/", views.cancel_pending_action),
    path("debuglog/<mode>/<hostname>/<order>/", views.debug_log),
    path("downloadlog/", views.download_log),
]
