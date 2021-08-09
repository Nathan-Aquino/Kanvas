from django.urls import path
from .views import AccountsView, ActivitiesView, CourseView, LoginView, SubmissionsView

urlpatterns = [
    path('accounts/', AccountsView.as_view()),
    path('login/', LoginView.as_view()),
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/', CourseView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseView.as_view()),
    path('activities/', ActivitiesView.as_view()),
    path('activities/<int:activity_id>/submissions/', SubmissionsView.as_view())
]