# from django.urls import include, path
# from rest_framework import routers
# from snippets import views
from django.contrib import admin
# # from snippets import views
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# # router.register(r'groups', views.GroupViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
# path('admin/', admin.site.urls),
# path('<int:pk>/', views.userlist),
#     path('test/', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),

    path('', include('snippets.urls')),
]
