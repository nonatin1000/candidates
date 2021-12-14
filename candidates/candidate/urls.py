from rest_framework import routers
from . import views


app_name = "candidate"

router = routers.SimpleRouter()
router.register(r'candidates', views.CandidateViewSet, basename="candidate")

urlpatterns = []

urlpatterns += router.urls
