from rest_framework import routers
from .api import JournalViewSet

router = routers.DefaultRouter()
router.register('api/journal', JournalViewSet, 'journal')


urlpatterns = router.urls
