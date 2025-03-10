from django.urls import path 

from . import views 

urlpatterns = [

    path('', views.home, name='home'),
    path('postits/', views.postit_index, name='postit-index'),
    path('postits/<int:postit_id>/', views.postit_detail, name='postit-detail'),
    path('postits/create', views.PostitCreate.as_view(), name='postit-create'),
    path('postits/<int:pk>/edit', views.PostitUpdate.as_view(), name='postit-update'),
    path('postits/<int:pk>/delete', views.PostitDelete.as_view(), name='postit-delete'), 
    path('postits/<int:postit_id>/add-reminder', views.add_reminder, name='add-reminder'),
    path('catagories/create', views.CatagoryCreate.as_view(), name='catagory-create'),
    path('catagories/<int:pk>', views.CatagoryDetail.as_view(), name='catagory-detail'),
    path('catagories', views.CatagoryList.as_view(), name='catagory-index'),
    path('catagories/<int:pk>/update', views.CatagoryUpdate.as_view(), name='catagory-update'),
    path('catagories/<int:pk>/delete', views.CatagoryDelete.as_view(), name='catagory-delete'),
    path('postits/<int:postit_id>/associate-catagory/<int:catagory_id>/', views.associate_catagory, name='associate-catagory'),
    path('postits/<int:postit_id>/remove-catagory/<int:catagory_id>/', views.remove_catagory, name='remove-catagory')

]