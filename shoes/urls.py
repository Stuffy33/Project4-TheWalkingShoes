from django.urls import path
from . import views


urlpatterns = [
    path('shoess/', views.ShoessPage.as_view(), name='shoess'),
    path('submitshoes/', views.submit_shoes, name='submit_shoe'),
    path('edit/<slug:slug>', views.edit_shoes, name='edit_shoe'),
    path('delete/<slug:slug>', views.delete_shoes, name='delete_shoe'),
    path('<slug:slug>/', views.ShoesDetails.as_view(), name='shoes_detail'),
    path('like/<slug:slug>', views.LikeShoePair.as_view(), name='like_shoe'),
]
