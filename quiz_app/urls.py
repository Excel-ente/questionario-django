from rest_framework.authtoken import views
from django.urls import path
from.views import Quiz, Result, send_email
from django.contrib.auth.views import LogoutView

app_name = 'quiz'
urlpatterns = [
    path('', Quiz.as_view(), name='quiz_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('result', Result.as_view(), name='result_page'),
    path('receive-result', send_email, name='send_email'),
]
