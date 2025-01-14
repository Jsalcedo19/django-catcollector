from django.urls import path

# import Home view from the views file
from .views import Home, CatList, CatDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('cats/', CatList.as_view(), name='cat-list'),
  path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),
]

