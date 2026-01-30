from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/accounts/", include("accounts.urls")),
    path('api/students/', include('students.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/registrations/', include('registrations.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/dashboard/', include('admin_dashboard.urls')),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

