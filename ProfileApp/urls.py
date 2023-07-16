
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


# namespace
app_name = 'profileapp'

urlpatterns = [

    # Function Based View
    path('', views.profileList, name='profile_list'),
    path('create/', views.profileCreate, name='profile_create'),
    path('<int:pk>/', views.profileDetail, name='profile_detail'),
    path('<int:pk>/update/', views.profileUpdate, name='profile_update'),
    path('<int:pk>/delete/', views.profileDelete, name='profile_delete'),
    path('<int:pk>/condelete/',views.confirmDelete,name='profile_condelete')


    # path('', views.ProfileListView.as_view(), name='profile_list'),
    # path('create/', views.ProfileCreateView.as_view(), name='profile_create'),
    # path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    # path('<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    # path('<int:pk>/delete/', views.profile_delete_view, name='profile_delete'),
    # path('<int:pk>/condelete/', views.confirm_delete_view, name='profile_condelete'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
