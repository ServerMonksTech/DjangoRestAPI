from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CategorySerializer
from .models import Category
# Create your views here.
from rest_framework.permissions import IsAuthenticated

class CategoryView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request,id=None):
        print(request.user.id)
        if id is not None:
            category = Category.objects.filter(id=id).values()
        else:
            category = Category.objects.all().values()
        return Response({"category": category})
    
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


