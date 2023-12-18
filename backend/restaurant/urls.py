from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')
router.register(r'users', views.UserViewSet, basename='users')


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', include(router.urls)),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),

    path('api-token-auth/', obtain_auth_token),
]
