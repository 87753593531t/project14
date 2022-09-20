from django.urls import re_path
from rest_framework.routers import DefaultRouter

from test15.views import StudentViewSet, StudentViewSet2


router = DefaultRouter()
router.register('students2', StudentViewSet)

urlpatterns = [
    re_path(r'^students/$', StudentViewSet2.as_view()),
    re_path(r'^students/(?P<id>[0-9]+)/$', StudentViewSet2.as_view()),
]+ router.urls
