from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'booklist', views.BookListViewSet,basename="Book")
router.register(r'bookdetail', views.BookDetailViewSet,basename="Book_detail")
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls',namespace='auth')),
]
