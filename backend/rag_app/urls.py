from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('load-sample/', views.load_sample_policy, name='load_sample_policy'),
    path('policy-pdf/', views.download_policy_pdf, name='download_policy_pdf'),
    path('chat/stream/', views.stream_chat_response, name='stream_chat_response'),
    path('session/new/', views.start_new_session, name='start_new_session'),
    path('session/delete-document/', views.delete_document, name='delete_document'),
    path('session/<str:session_id>/', views.get_session_details, name='get_session_details'),
    path('evaluate/', views.run_evaluation_suite, name='run_evaluation_suite'),
]
