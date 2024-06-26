from django.urls import include, path

# from cats.views import cat_list, cat_detail
# from cats.views import APICat
# from cats.views import CatList, CatDetail
from cats.views import CatViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   # path('cats/', cat_list),
   # path('cats/<int:pk>/', cat_detail),
   # path('cats/', APICat.as_view()),
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view()),
   path('', include(router.urls)),
]
