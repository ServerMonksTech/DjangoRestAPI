from django.urls import path
from .views import create_category,delete_category
urlpatterns = [
    path("create-category/", create_category, name="create-category"),
    path("delete-category/<int:id>", delete_category, name="delete-category"),
]
