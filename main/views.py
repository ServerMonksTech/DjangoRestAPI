from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
# Create your views here.

@api_view(['POST'])
def create_category(request):
    category_name = request.data.get('category')
    cat = Category.objects.create(name=category_name)
    cat_data = Category.objects.all().values()
    return Response({"data": cat_data})


@api_view(['DELETE'])
def delete_category(request,id):
    Category.objects.filter(id=id).delete()
    cat_data = Category.objects.all().values()
    return Response({"data": cat_data})
