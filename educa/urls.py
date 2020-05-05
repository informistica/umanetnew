from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('forum/', include('forum.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
