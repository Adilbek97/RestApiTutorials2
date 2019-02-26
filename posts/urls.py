from rest_framework import routers
from .api.viewsets import LeadViewSet,BookViewSet, TeacherViewSet, StudentViewSet, SubjectViewSet, QuestionsViewSet, ResultViewSet

router = routers.DefaultRouter()
router.register('api/leads',LeadViewSet,'leads')
router.register('api/books',BookViewSet,'books')
router.register('api/teachers',TeacherViewSet)
router.register('api/students',StudentViewSet,'students')
router.register('api/subjects',SubjectViewSet,'subjects')
router.register('api/questions',QuestionsViewSet,'questions')
router.register('api/results',ResultViewSet,'results')


urlpatterns = router.urls