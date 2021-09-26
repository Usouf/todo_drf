from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from api.views import TaskView
# from OneToOne import views


# admin.autodiscover()
router = routers.DefaultRouter()
router.register('tasks', TaskView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('', include('frontend.urls'))
]

# urlpatterns += format_suffix_patterns([
#     # API to map the student record
#     path('api/tasks/',
#         TaskView.as_view(),
#         name='tasks_list'),
# ])
