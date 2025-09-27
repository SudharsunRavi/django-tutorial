from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Blog
from .serializers import BlogSerializer

# POST (create), GET (all)
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# GET (single with id), PUT/PATCH, DELETE
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
