from django.urls import path
from .views import get_products, render_image

urlpatterns = [
    path('api/products/', get_products),
    path('api/render/', render_image),
]