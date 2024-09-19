from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AssessmentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'assessments', AssessmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from .views import UserRegistrationView, UserLoginView

urlpatterns += [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]