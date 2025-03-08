from django.urls import path 

from . import views 

urlpatterns = [

    path('', views.home, name='home'),
    path('postits/', views.postit_index, name='postit-index'),
    path('postits/<int:postit_id>/', views.postit_detail, name='postit-detail'),
    path('postits/create', views.PostitCreate.as_view(), name='postit-create'),
    path('postits/<int:pk>/edit', views.PostitUpdate.as_view(), name='postit-update'),
    path('postits/<int:pk>/delete', views.PostitDelete.as_view(), name='postit-delete'),
]