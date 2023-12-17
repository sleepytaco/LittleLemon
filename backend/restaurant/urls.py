from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', include(router.urls)),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
]
