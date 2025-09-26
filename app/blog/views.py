from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

# POST (create), GET (all)
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# GET (single with id), PUT/PATCH, DELETE
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
