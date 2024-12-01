from django.urls import path
from .views import ItemListCreateAPIViewData, ItemDetailAPIViewData

urlpatterns = [
    path("items/", ItemListCreateAPIViewData.as_view(), name="item-list-create"),
    path("items/<int:id>/", ItemDetailAPIViewData.as_view(), name="item-detail"),
]



