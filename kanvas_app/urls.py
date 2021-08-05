from django.urls import path
from .views import AccountsView, CourseView, LoginView

urlpatterns = [
    path('accounts/', AccountsView.as_view()),
    path('login/', LoginView.as_view()),
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseView.as_view())
]