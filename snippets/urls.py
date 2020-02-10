from django.urls import path,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
#
# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# ]

urlpatterns = [
    path('snippets/', views.SnippetList2.as_view()),
    path('example/', views.ExampleView.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail2.as_view(),name='snippets-detail'),
    # path('api-auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
path('api-token-auth/', obtain_auth_token, name='api_token_auth'),



]
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
