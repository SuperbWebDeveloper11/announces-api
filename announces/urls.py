from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    # announces routers
    path('', views.AnnounceList.as_view()),
    path('<int:pk>/', views.AnnounceDetail.as_view()),
    # comments routers
    path('<int:pk>/comments/', views.CommentList.as_view()),
    path('<int:pk>/comments/<int:comment_pk>/', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

