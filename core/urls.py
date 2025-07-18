from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet, job_list_view, my_applications_view, user_login_view, user_logout_view, apply_job
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('jobs', JobViewSet)
router.register('applications', ApplicationViewSet)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/', include(router.urls)),
    
    # UI Routes
    path('login/', user_login_view, name='user_login'),
    path('logout/', user_logout_view, name='user_logout'),
    path('jobs/', job_list_view, name='job_list'),
    path('jobs/apply/<int:job_id>/', apply_job, name='apply_job'),
    path('my-applications/', my_applications_view, name='my_applications'),
]
