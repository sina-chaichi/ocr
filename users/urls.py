from django.urls import path

from website import views
from website.views import views_process

app_name = 'users'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('model_form_upload/',views.model_form_upload,name='model_form_upload'),
    path('process/',views_process.process,name='process')
]
